# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from application import settings
from question.forms import CreateQuestionForm
from question.models import Questions, Categories


class CategoriesList(ListView):
    model = Categories
    template_name = 'question/categories_list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Categories
    template_name = 'question/category_detail.html'
    context_object_name = 'category'


class QuestionList(ListView):
    model = Questions
    template_name = 'question/questions_list.html'
    context_object_name = 'questions'


class QuestionDetail(DetailView):
    model = Questions
    template_name = 'question/question_detail.html'
    context_object_name = 'question'


class CreateQuestionView(LoginRequiredMixin, CreateView):
    login_url = settings.LOGIN_URL
    form_class = CreateQuestionForm
    model = Questions
    template_name = 'question/create_question.html'

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateQuestionView, self).form_valid(form)
