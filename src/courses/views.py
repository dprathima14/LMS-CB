from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def course_home(request):
	#form = LoginForm(request.POST or None)
	queryset = Course.objects.all()
	context = {
		"object_list": queryset,
		"title": "Courses",
	}
	return render(request, "course_home.html", context)