# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from application import settings
from question.models import Questions


class Answers(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='answer_author')
    question = models.ForeignKey(Questions, verbose_name='Вопрос', related_name='answers')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(default='', verbose_name='Текст вопроса')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
