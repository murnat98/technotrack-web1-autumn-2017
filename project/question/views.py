# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from application import settings
from question.forms import CreateQuestionForm, CreateAnswerForm
from question.models import Questions, Categories, Answers


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


class QuestionDetail(CreateView):
    model = Answers
    template_name = 'question/question_detail.html'
    form_class = CreateAnswerForm

    def __init__(self, **kwargs):
        super(QuestionDetail, self).__init__(**kwargs)
        self.question = None

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = get_object_or_404(Questions, id=self.kwargs['pk'])

        return super(QuestionDetail, self).form_valid(form)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Questions, id=pk)

        return super(QuestionDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)

        context['question'] = self.question

        return context


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
