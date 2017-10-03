# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def main(request):

    return render(request, "main.html")


def about(request):

    return render(request, "about.html")


def portfolio(request):

    return render(request, "portfolio.html")


def portfolio_images(request, image_name):

    return render(request, "portfolio_images.html", {"image_name": image_name})


def advertising(request):

    return render(request, "advertising.html")


def advertising_images(request, image_name):
    return render(request, "advertising_images.html", {"image_name": image_name})


def editorial(request):

    return render(request, "editorial.html")


def editorial_images(request, image_name):

    return render(request, "editorial_images.html", {"image_name": image_name})


def contacts(request):

    return render(request, "contacts.html")
