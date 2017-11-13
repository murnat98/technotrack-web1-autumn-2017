# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from question.models import Questions


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass
