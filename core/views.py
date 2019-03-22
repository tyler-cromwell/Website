from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views import generic

from . import models


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def posts(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .order_by('-published_date')
    template = loader.get_template('posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))


def books(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.BOOKS) \
            .order_by('-published_date')
    template = loader.get_template('posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))


def programming(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.PROGRAMMING) \
            .order_by('-published_date')
    template = loader.get_template('posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))


def travel(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.TRAVEL) \
            .order_by('-published_date')
    template = loader.get_template('posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))


def details(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    template = loader.get_template('details.html')
    context = {
        'post': post,
        'category': post.category,
        'books': models.BOOKS,
        'programming': models.PROGRAMMING,
        'travel': models.TRAVEL
    }
    return HttpResponse(template.render(context, request))
