from django.db import models
from django.conf import settings
from assignments.models import Assignment
from django.core.urlresolvers import reverse

#User = settings.AUTH_USER_MODEL
# Create your models here.
class Course(models.Model):
    assignments = models.ManyToManyField(Assignment, blank=True)
    course_code = models.CharField(max_length=120)
    course_title = models.CharField(max_length=120)
    course_description = models.TextField(blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    syllabus	= models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
    	return reverse("courses:detail", kwargs={"id": self.id})