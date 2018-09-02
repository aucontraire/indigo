# encoding: utf-8

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.utils import timezone


def home_page(request):
    return render(request, 'home.html')

