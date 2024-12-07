from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'contents', 'assignments']
        widgets = {
            'contents': forms.CheckboxSelectMultiple(),
            'assignments': forms.CheckboxSelectMultiple(),
        }
