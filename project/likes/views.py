# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import HttpResponse
from django.views import View

from question.models import Answers


class LikeView(View):
    def post(self, request, pk=None):
        answer = Answers.objects.get(id=pk)

        if request.user.is_authenticated:
            Answers.objects.filter(id=pk).update(likes_count=models.F('likes_count') + 1)

        likes_count = answer.likes_count + 1

        return HttpResponse(likes_count)
