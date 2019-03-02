from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('core/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('core/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def posts(request):
    template = loader.get_template('core/posts.html')
    context = {}
    return HttpResponse(template.render(context, request))
