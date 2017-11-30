from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def student_list(request, cid=None):
	#form = LoginForm(request.POST or None)
	#user = User(id=request.user.id)
	queryset = User.objects.all().filter(staff=False, courses__id=cid).order_by('username')
	#queryset = user.courses(id=id)
	context = {
		"object_list": queryset,
		"title": "Student List",
		"id": cid,
	}
	return render(request, "account/student_list.html", context)

def user_details(request, cid=None, user=None):
	#form = LoginForm(request.POST or None)
	user = get_object_or_404(User, id=user)
	queryset = user.courses.all()

	context = {
		"name": user.username,
		"user": user,
		"courses": queryset,
		"id": cid,
	}
	return render(request, "account/student_detail.html", context)

def user_profile(request):
	#form = LoginForm(request.POST or None)
	user = get_object_or_404(User, id=request.user.id)
	queryset = user.courses.all()

	context = {
		"name": user.username,
		"user": user,
		"courses": queryset,
	}
	return render(request, "account/user_profile.html", context)

