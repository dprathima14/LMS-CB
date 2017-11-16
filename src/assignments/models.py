from django.db import models

# Create your models here.
class Assignment(models.Model):
#    user        = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=120)
    due_date = models.DateTimeField()
    points	= models.IntegerField()
    assigment_description = models.TextField(blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)