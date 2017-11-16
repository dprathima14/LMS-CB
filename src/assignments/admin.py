from django.contrib import admin

# Register your models here.
from .models import Assignment

class AssignmentModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "title", "due_date", "points"]
	search_fields = ["title"]
	ordering = ["due_date"]
	class Meta:
		model = Assignment

admin.site.register(Assignment, AssignmentModelAdmin)
