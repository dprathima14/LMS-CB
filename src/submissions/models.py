from django.db import models

from courses.models import Course
from accounts.models import User
from assignments.models import Assignment


# Create your models here.
class Submission(models.Model):
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    assignment = models.ForeignKey(Assignment)
    submission	= models.FileField(null=True, blank=True)
    points	= models.IntegerField(null=True, blank=True)
    total_points	= models.IntegerField(null=True, blank=True)
    comments = models.TextField(blank=True)
    updated	= models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
