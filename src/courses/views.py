from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course
from accounts.models import User

# Create your views here.
def course_home(request):
	#form = LoginForm(request.POST or None)
	user = User(id=request.user.id)
	queryset = user.courses.all()
	context = {
		"object_list": queryset,
		"title": "Courses",
	}
	return render(request, "course_home.html", context)


def course_detail(request, cid=None):
	#form = LoginForm(request.POST or None)
	instance = get_object_or_404(Course, id=cid)
	context = {
		"title": instance.course_title,
		"instance": instance,
	}
	return render(request, "course_detail.html", context)