from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from courses.models import Course

# Create your models here.
class Assignment(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=120, unique=True)
	due_date = models.DateTimeField()
	total_points	= models.IntegerField()
	description = models.TextField(blank=True)
	updated     = models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	question	= models.FileField(null=True, blank=True)
	publish		= models.BooleanField(default=False)
    #course = models.ForeignKey(Course)

	def __str__(self):
		return str(self.title)

	def is_past_due(self):
		return timezone.now() > self.due_date

	def get_absolute_url(self):
		return reverse("assignments:assignment_detail", kwargs={"aid": self.id})