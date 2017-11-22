from django.conf.urls import include, url
from .views import student_list, user_details, user_profile

urlpatterns = [
    url(r'^students/$', student_list, name="student_list"),
    url(r'^students/(?P<user>\d+)/$', user_details, name="detail"),
    url(r'^$', user_profile, name="user_profile"),
] 
