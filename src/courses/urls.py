from django.conf.urls import include, url
from .views import course_home

urlpatterns = [
    url(r'^$', course_home, name="course_home"),
] 
