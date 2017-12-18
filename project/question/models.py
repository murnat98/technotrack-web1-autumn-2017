# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from application import settings


class Categories(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Название категории')

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class QuestionQuerySet(models.QuerySet):
    def annotate_answers_count(self):
        return self.annotate(answers_count=models.Count('answers__id'))


class Questions(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='question_author')
    category = models.ManyToManyField(Categories, related_name='questions', verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(default='', verbose_name='Текст')
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = QuestionQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-posted_date', ]


class Answers(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='answer_author')
    question = models.ForeignKey(Questions, verbose_name='Вопрос', related_name='answers')
    text = models.TextField(default='', verbose_name='Ответ')
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-posted_date', ]
