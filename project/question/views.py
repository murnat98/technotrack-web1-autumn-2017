# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from application import settings
from question.forms import CreateQuestionForm, CreateAnswerForm, UpdateQuestionForm, UpdateAnswerForm
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


class QuestionDetail(CreateView):  # really question detail and creating answer
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


class UpdateAnswerView(LoginRequiredMixin, UpdateView):
    login_url = settings.LOGIN_URL
    form_class = UpdateAnswerForm
    model = Answers
    template_name = 'question/update_answer.html'

    def __init__(self, **kwargs):
        super(UpdateAnswerView, self).__init__(**kwargs)
        self.question = None

    def get_success_url(self):
        question_pk = self.question.pk
        return reverse('questions:question_detail', kwargs={'pk': question_pk}) + '#answer_' + str(question_pk)

    def get_queryset(self):
        return super(UpdateAnswerView, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        self.question = form.instance.question
        return super(UpdateAnswerView, self).form_valid(form)


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


class UpdateQuestionView(LoginRequiredMixin, UpdateView):
    login_url = settings.LOGIN_URL
    template_name = 'question/update_question.html'
    model = Questions
    form_class = UpdateQuestionForm

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return super(UpdateQuestionView, self).get_queryset().filter(author=self.request.user)


def my_questions(request):
    return render(request, 'question/my_questions.html')


def my_answers(request):
    return render(request, 'question/my_answers.html')
