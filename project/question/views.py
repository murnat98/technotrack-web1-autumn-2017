# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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

    def get_queryset(self):
        return super(CategoryDetail, self).get_queryset().prefetch_related('questions__author')


class QuestionList(ListView):
    model = Questions
    template_name = 'question/questions_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return super(QuestionList, self).get_queryset().select_related('author')


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
        self.question = get_object_or_404(
            Questions.objects.prefetch_related('answers', 'answers__author').select_related('author'),
            id=pk
        )

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


class MyQuestionsList(ListView):
    model = Questions
    template_name = 'question/my_questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return super(MyQuestionsList, self).get_queryset().filter(author=self.request.user).select_related('author')


class MyAnswersList(ListView):
    model = Answers
    template_name = 'question/my_answers.html'
    context_object_name = 'answers'

    def get_queryset(self):
        return super(MyAnswersList, self).get_queryset().filter(author=self.request.user).select_related('question')
