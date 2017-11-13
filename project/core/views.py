# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView, DetailView

from application.settings import LOGIN_REDIRECT_URL
from core.forms import LoginForm, RegisterForm
from core.models import User


def main(request):
    return render(request, 'core/main.html')


def show_users(request):
    users = User.objects.all()

    return render(request, 'core/show_users.html', {'users': users})


def show_user(request, user_id):
    requested_user = get_object_or_404(User.objects.all(), id=user_id)
    # user_posts = Restaurant.objects.filter(author=requested_user)
    user_posts = None

    return render(request, 'core/show_user.html', {'requested_user': requested_user, 'user_posts': user_posts})


class Login(LoginView):
    template_name = 'core/login.html'
    form_class = LoginForm
    redirect_authenticated_user = LOGIN_REDIRECT_URL  # TODO: login after registering


class Register(FormView):
    form_class = RegisterForm
    success_url = '/'
    template_name = 'core/register.html'

    def dispatch(self, request, *args, **kwargs):
        authenticate(request)

        return super(Register, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()

        return super(Register, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')
