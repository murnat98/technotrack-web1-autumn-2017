# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from likes.models import Like


@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    pass
