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


class Questions(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор')
    category = models.ManyToManyField(Categories, related_name='questions', verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(default='', verbose_name='Текст')
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
