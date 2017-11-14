# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from question.models import Questions, Categories


class CategoriesList(ListView):
    model = Categories
    template_name = 'question/categories_list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Categories
    template_name = 'question/category_detail.html'
    context_object_name = 'category'


class QuestionDetail(DetailView):
    model = Questions
    template_name = 'question/question_detail.html'
    context_object_name = 'question'
