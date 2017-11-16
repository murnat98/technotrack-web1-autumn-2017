from django import forms
from django.http import request

from question.models import Questions, Answers


question_fields = ['category', 'title', 'text']
answer_fields = ['title', 'text']


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = question_fields


class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = question_fields


class UpdateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = answer_fields


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['title', 'text']
