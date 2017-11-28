# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView, DetailView

from application.settings import LOGIN_REDIRECT_URL
from core.forms import LoginForm, RegisterForm
from core.models import User
from question.models import Questions


def main(request):
    return render(request, 'core/main.html')


def show_users(request):
    users = User.objects.all()

    return render(request, 'core/show_users.html', {'users': users})


class UserDetail(DetailView):
    template_name = 'core/user_detail.html'
    model = User
    context_object_name = 'username'


class Login(LoginView):
    template_name = 'core/login.html'
    form_class = LoginForm
    redirect_authenticated_user = LOGIN_REDIRECT_URL  # TODO: login after registering


class Register(FormView):
    form_class = RegisterForm
    success_url = '/'
    template_name = 'core/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(Register, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')
