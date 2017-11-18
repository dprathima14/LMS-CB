from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import login

def home(request):
	if request.user.is_authenticated:
		return redirect('/courses')
	else: 
		return redirect(login)
#def login_page(request):
	#form = LoginForm(request.POST or None)
#	context = {
	#	"title" : "welcome",
	#	"form": form,
#	}
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#	username = request.POST.get('email', '')
#	password = request.POST.get('password', '')
#	user = authenticate(username=username, password=password)
#	if user is not None:
#		login(request, user)
#		return redirect('/courses')
#	else:
	# Return an 'invalid login' error message.
		#raise forms.ValidationError("Invalid credentials")
#		print("Error")
#		return render(request, "login.html", context)

#	return render(request, "login.html", context)
#def logout_page(request):
#	logout(request)
#	return render(request, "logout.html", {})

def help_page(request):
	return render(request, "help.html", {})