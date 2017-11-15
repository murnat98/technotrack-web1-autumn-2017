from django import forms
from django.http import request

from question.models import Questions


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['category', 'title', 'text']
