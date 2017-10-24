# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from ads.models import Restaurant
from core.models import User


def main(request):
    return render(request, 'core/main.html')


def show_users(request):
    users = User.objects.all()

    return render(request, 'core/show_users.html', {'users': users})


def show_user(request, user_id):
    user = get_object_or_404(User.objects.all(), id=user_id)
    user_posts = Restaurant.objects.filter(author=request.user)

    return render(request, 'core/show_user.html', {'user': user, 'user_posts': user_posts})
