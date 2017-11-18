from django.conf.urls import include, url
from .views import course_home, course_detail

urlpatterns = [
    url(r'^$', course_home, name="course_home"),
    url(r'^(?P<id>\d+)/$', course_detail, name="detail"),
] 
