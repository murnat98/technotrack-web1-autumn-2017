# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from core.models import User


class Base(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(name='title', verbose_name='загаловок', max_length=100)
    company = models.CharField(name='company', verbose_name='компания', max_length=100)
    description = models.TextField(name='description', verbose_name='описание', default='')
    price = models.IntegerField(name='price', verbose_name='цена')
    date_added = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-date_added',)
        abstract = True


"""
==============Categories==============
"""


class Restaurant(Base):
    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
        abstract = False


categories = {
    'restaurant': Restaurant,
}

"""
==============Categories==============
"""
