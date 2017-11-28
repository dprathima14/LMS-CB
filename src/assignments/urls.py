from django.conf.urls import url
from .views import assignment_home, assignment_detail

urlpatterns = [
	url(r'^$', assignment_home, name="assignment_home"),
	url(r'^(?P<aid>\d+)/$', assignment_detail, name="assignment_detail"),
#	url(r'^(?P<aid>\d+)/$', add_assignment, name="add_assignment"),
]
