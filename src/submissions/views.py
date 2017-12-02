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
	#student_submission_points = set()
	student_submission_total = set()
	students = User.objects.all().filter(staff=False, courses__id=cid)
	for student in students:
		points = Submission.objects.all().filter(course__id=cid, user__id=student.id).aggregate(sum=Sum('points'))['sum']
#		total_points = Submission.objects.all().filter(course__id=cid, user__id=student.id).aggregate(total=Sum('total_points'))['total']

#		if points and total_points:
#			div = points / total_points
#		else:
#			div = 0
		student_submission_total.add(points)

	courses = Course.objects.all()
	context = {	
	    "students": students,
	    "total": student_submission_total,
		"id": cid,	
	}

	return render(request, "submission/instructor_grade.html", context)