from django import forms
from django.forms import ModelForm
from .models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'course_length', 'art']
        widgets = { 'course_length': forms.RadioSelect, }
