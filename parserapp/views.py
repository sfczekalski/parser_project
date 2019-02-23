from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Page


def home(request):
    return HttpResponse("<h1>Home</h1>")


class ProvideUrl(CreateView):
    model = Page
    fields = ['url_address']


class DetailUrl(DetailView):
    model = Page
