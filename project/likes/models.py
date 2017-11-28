# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from application import settings
from question.models import Answers


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', related_name='user')
    answer = models.ForeignKey(Answers, verbose_name='Ответ', related_name='answers')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
