from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def posts(request):
    posts = Post.objects.order_by('-published_date')
    template = loader.get_template('posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))
