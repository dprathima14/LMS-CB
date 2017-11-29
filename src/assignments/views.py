from django.shortcuts import render
from courses.models import Course
from .models import Assignment
from accounts.models import *

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
		return render(request, "assignment_home.html", context)
	else:
		return render(request, "assignment_home_student.html", context)


def assignment_detail(request, cid=None, aid=None):
	#if request.method == "POST":
	instance = Assignment.objects.get(id=aid)
	#	instance.save()

	#assignments = Assignment.objects.all().filter(course__id=cid)
	context = {
		"instance": instance,
		"id": cid,
	}
	return render(request, "assignment_detail.html", context)

