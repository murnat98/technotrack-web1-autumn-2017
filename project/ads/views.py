# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from ads.models import *
from ads.functions.get_object_by_name import get_object_by_name


def category_view(request, category):
    category_object = get_object_by_name(category, categories).objects.all()

    return render(request, 'ads/category_view.html', {'category_object': category_object})


def post_detail(request, category, post_id):
    category_object = get_object_by_name(category, categories)
    post = get_object_or_404(category_object, id=post_id)

    return render(request, 'ads/post_detail.html', {'post': post})
