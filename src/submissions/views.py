from django.shortcuts import render
from assignments.models import Assignment
from courses.models import Course
from .models import Submission

# Create your views here.
def assignment_list(request, cid=None):
	#form = LoginForm(request.POST or None)
	#user = User(id=request.user.id)
	course = Course(id=cid)
	queryset = course.assignments.all().order_by('due_date')

	context = {
		"object_list": queryset,
		"title": "Assignment List",
		"id": course.id,
	}
	return render(request, "assignment_list.html", context)

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
	return render(request, "submissions.html", context)
