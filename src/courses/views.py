from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm
from django.http import HttpResponse
from .models import Course
from accounts.models import User
from assignments.models import Assignment
#from django.core.files.storage import FileSystemStorage

# Create your views here.
def course_home(request):
	user = User(id=request.user.id)
	assignments = Assignment.objects.all().order_by('due_date')
	courses = user.courses.all()
	context = {
		"object_list": courses,
		"todo": assignments,
		"title": "Courses",
	}
	return render(request, "course/course_home.html", context)


def course_detail(request, cid=None):
	#form = LoginForm(request.POST or None)
	instance = get_object_or_404(Course, id=cid)
	context = {
		"title": instance.course_title,
		"instance": instance,
	}
	return render(request, "course/course_detail.html", context)


def syllabus_view(request, cid=None):
	instance = get_object_or_404(Course, id=cid)
	context = {
		"title": instance.course_title,
		"instance": instance,
	}
	return render(request, "course/syllabus.html", context)

def syllabus_upload(request, cid=None):
	course = Course.objects.get(id=cid)
	if request.method == "POST":
		form = CourseForm(request.POST or None, request.FILES or None, instance=course)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect("courses:detail",cid=cid)
	else:
		form = CourseForm(instance=course)

	context = {
		"form": form,
		"id" : cid,
	}
	return render(request, "course/syllabus_upload.html", context)

        
