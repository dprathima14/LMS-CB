from django.conf.urls import url
from .views import assignment_home, assignment_detail, assignment_submitted, assignment_edit, assignment_create

urlpatterns = [
	url(r'^$', assignment_home, name="assignment_home"),
	url(r'^(?P<aid>\d+)/$', assignment_detail, name="assignment_detail"),
	url(r'^(?P<aid>\d+)/edit/$', assignment_edit, name="assignment_edit"),
	url(r'^submitted/$', assignment_submitted, name="assignment_list"),
	url(r'^create/$', assignment_create, name="assignment_create"),
]
