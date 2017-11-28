# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from likes.models import Like
from question.models import Answers


class LikeView(View):
    def post(self, request, pk=None):
        obj, created = Like.objects.get_or_create(
            user=request.user,
            answer_id=pk,
        )

        result = obj.answer.answers.all().count()
        return HttpResponse(result)
