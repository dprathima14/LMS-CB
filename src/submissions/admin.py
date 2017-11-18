from django.contrib import admin

# Register your models here.
from .models import Submission

class SubmissionModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "course", "user", "assignment"]
	search_fields = ["assignment"]
	class Meta:
		model = Submission

admin.site.register(Submission, SubmissionModelAdmin)