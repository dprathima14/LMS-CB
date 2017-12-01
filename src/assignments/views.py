from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from .models import Assignment
from accounts.models import *
from .forms import AssignmentForm

# Create your views here.
def assignment_home(request, cid=None):
	course = Course(id=cid)
	all_assignment = course.assignments.all().order_by('due_date')
	upcoming_assignment = set()
	overdue_assignment = set()
	for c in all_assignment:
		if c.is_past_due() is False:
			upcoming_assignment.add(c)
		else:
			overdue_assignment.add(c)

	context = {
		"upcoming_assignment": upcoming_assignment,
		"overdue_assignment": overdue_assignment,
		"title": "Assignment List",
		"id": course.id,
	}
	if request.user.is_staff == True:
		return render(request, "assignment/assignments_instructor.html", context)
	else:
		return render(request, "assignment/assignments_student.html", context)


def assignment_edit(request, cid=None, aid=None):
	instance = get_object_or_404(Assignment, id=aid)
	if request.method == "POST":
		form = AssignmentForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect("courses:assignments:assignment_home", cid=cid)
	else:
		form = AssignmentForm(instance=instance)
	context = {
		"form": form,
		"id": cid,
	}
	return render(request, "assignment/assignment_edit.html", context)


def assignment_detail(request, cid=None, aid=None):
	instance = get_object_or_404(Assignment, id=aid)
	context = {
		"instance": instance,
		"id": cid,
	}
	return render(request, "assignment/assignment_detail.html", context)

def assignment_submitted(request, cid=None):
	#form = LoginForm(request.POST or None)
	#user = User(id=request.user.id)
	course = Course(id=cid)
	queryset = course.assignments.all().order_by('due_date')

	context = {
		"object_list": queryset,
		"id": course.id,
	}
	return render(request, "assignment/assignments_submitted.html", context)

def assignment_create(request, cid=None):
	if request.method=="POST":
		form = AssignmentForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save()
			course = Course.objects.get(id=cid)
			course.assignments.add(instance)
			course.save()
			return redirect("courses:assignments:assignment_home", cid=cid)
	else: 
		form = AssignmentForm(None)
	context = {
		"form": form,
		"id": cid,
	}
	return render(request, "assignment/assignment_create.html", context)
