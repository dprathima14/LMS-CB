from django.shortcuts import render, get_object_or_404, redirect
from assignments.models import Assignment
from django.db.models import Sum
from courses.models import Course
from accounts.models import User
from .models import Submission
from .forms import SubmissionForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def submission_list(request, cid=None, aid=None):
	if request.method == "POST":
		instance = Submission.objects.get(id=request.POST.get('sid'))
		instance.points = request.POST.get('points')
		if int(instance.points) > int(instance.assignment.total_points):
			instance.points = instance.assignment.total_points
		instance.save()

	submissions = Submission.objects.all().filter(course__id=cid, assignment__id=aid)
	context = {
		"object_list": submissions,
		"id": cid,
	}

	return render(request, "submission/submissions.html", context)

def submit_assignment(request, cid=None, aid=None):
	try:
		submission = Submission.objects.get(course__id=cid, assignment__id=aid, user__id=request.user.id)
	except ObjectDoesNotExist:
		submission = None
	
	if request.method == "POST":
		if submission:
			form = SubmissionForm(request.POST or None, request.FILES or None, instance=submission)
		else:
			form = SubmissionForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			if submission == None:
				instance.user = User.objects.get(id=request.user.id)
				instance.course = Course.objects.get(id=cid)
				instance.assignment = Assignment.objects.get(id=aid)
				instance.total_points = instance.assignment.total_points
			instance.save()
			return redirect("courses:assignments:assignment_home", cid=cid)
	else:
		if submission:
			form = SubmissionForm(instance=submission)
		else: 
			form = SubmissionForm(request.POST or None, request.FILES or None)
	context = {
		"form": form,
		"id": cid,
	}

	return render(request, "submission/submit_assignment.html", context)

def student_grade(request, cid=None):
	submissions = Submission.objects.all().filter(course__id=cid, user__id=request.user.id)
	points = Submission.objects.all().filter(course__id=cid, user__id=request.user.id).aggregate(sum=Sum('points'))['sum']
	total_points = Submission.objects.all().filter(course__id=cid, user__id=request.user.id).aggregate(total=Sum('total_points'))['total']
	context = {
		"object_list": submissions,
		"points": points,
		"total": total_points,
		"id": cid,	
	}

	return render(request, "submission/student_grade.html", context)


def instructor_grade(request, cid=None):
	students = User.objects.all().filter(staff=False, courses__id=cid)
	scored_points_list = []
	student_list = []
	for student in students:
		submissions = Submission.objects.all().filter(course__id=cid, user__id=student.id)
		points = 0
		total_points = 0
		for sub in submissions:
			if sub.points:
				points += sub.points
				total_points += sub.assignment.total_points
		
		if total_points == 0:
			total = 0		
		else:
			total = (points/total_points) * 100 

		scored_points_list.append(total)
		student_list.append(student.email) 

#	print("student points list = {0}".format(scored_points_list))
#	print("student list = {0}".format(student_list))	
	courses = Course.objects.all()
	context = {	
		"students": student_list,
		"total": scored_points_list,
		"id": cid,	
	}

	return render(request, "submission/instructor_grade.html", context)