# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from question.models import Questions, Categories, Answers


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass
