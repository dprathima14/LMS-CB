from django.conf.urls import include, url
from .views import course_home, course_detail

urlpatterns = [
    url(r'^$', course_home, name="course_home"),
    url(r'^(?P<cid>\d+)/$', course_detail, name="detail"),
    url(r'^(?P<cid>\d+)/submissions/', include("submissions.urls", namespace="submissions")),
    url(r'^(?P<cid>\d+)/accounts/', include("accounts.urls", namespace="accounts")),
] 
