from django import forms

from .models import Assignment

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['title', 'due_date', 'total_points', 'description', 'question', 'publish']
