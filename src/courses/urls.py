from django.conf.urls import include, url
from .views import course_home, course_detail, syllabus_view

urlpatterns = [
    url(r'^$', course_home, name="course_home"),
    url(r'^(?P<cid>\d+)/$', course_detail, name="detail"),
    url(r'^(?P<cid>\d+)/submissions/', include("submissions.urls", namespace="submissions")),
    url(r'^(?P<cid>\d+)/accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^(?P<cid>\d+)/syllabus/$', syllabus_view, name="syllabus_view"),
    url(r'^(?P<cid>\d+)/assignments/', include("assignments.urls", namespace="assignments")),
]