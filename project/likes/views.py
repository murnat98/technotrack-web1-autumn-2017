# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from likes.models import Like
from question.models import Answers


class LikeView(View):
    def __init__(self, **kwargs):
        super(LikeView, self).__init__(**kwargs)
        self.obj = None

    def post(self, request, pk=None):
        self.obj = get_object_or_404(Answers, id=pk)

        if not Like.objects.filter(user=request.user, answer=self.obj).exists():
            likes = Like(user=request.user, answer=self.obj)
            likes.save()

        return HttpResponse(Like.objects.filter(answer=self.obj).count())
