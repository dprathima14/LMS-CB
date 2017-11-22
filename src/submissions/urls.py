from django.conf.urls import url
from .views import assignment_list, submission_list

urlpatterns = [
    url(r'^$', assignment_list, name="assignment_list"),
    url(r'^(?P<aid>\d+)$', submission_list, name="submission_list"),
] 