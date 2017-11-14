# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0002_auto_20171114_0904'),
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='question.Questions', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
            preserve_default=False,
        ),
    ]
