from django.contrib import admin

# Register your models here.
from .models import Course

class CourseModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "course_code", "course_title"]
	search_fields = ["course_code", "course_title"]
	class Meta:
		model = Course

admin.site.register(Course, CourseModelAdmin)
