from django import forms
from django.http import request

from question.models import Questions, Answers


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['category', 'title', 'text']


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['title', 'text']
