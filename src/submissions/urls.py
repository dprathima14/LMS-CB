from django.conf.urls import url
from .views import submission_list, submit_assignment, student_grade, instructor_grade

urlpatterns = [
    url(r'^(?P<aid>\d+)$', submission_list, name="submission_list"),
    url(r'^(?P<aid>\d+)/submit/$', submit_assignment, name="submit_assignment"),
    url(r'^grades/$', student_grade, name="student_grade"),
    url(r'^gradebook/$', instructor_grade, name="instructor_grade"),
] 