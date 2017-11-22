from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Assignment(models.Model):
#    user        = models.ManyToManyField(User, blank=True)
	title = models.CharField(max_length=120)
	due_date = models.DateTimeField()
	total_points	= models.IntegerField()
	assigment_description = models.TextField(blank=True)
	updated     = models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	question	= models.FileField(null=True, blank=True)

	def __str__(self):
		return str(self.title)

	def is_past_due(self):
		return timezone.now() > self.due_date