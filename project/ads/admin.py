# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ads.models import Restaurant


@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):

    pass
