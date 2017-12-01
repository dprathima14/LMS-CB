from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm
from django.http import HttpResponse
from .models import Course
from accounts.models import User
#from django.core.files.storage import FileSystemStorage

# Create your views here.
def course_home(request):
	#form = LoginForm(request.POST or None)
	user = User(id=request.user.id)
	queryset = user.courses.all()
	context = {
		"object_list": queryset,
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
	return render(request, "course/syllabus_instructor.html", context)

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
		return render(request, "course/syllabus_upload.html",context)

'''
def syllabus_upload(request):
	if request.method == 'POST' and request.FILES['upload']:
		myfile = request.FILES['upload']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'test.html', {
            'uploaded_file_url': uploaded_file_url
        })
'''
        
