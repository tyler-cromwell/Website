from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views import generic

from . import models


def _inner_view(request, name, context={}):
    template = loader.get_template(name)
    return HttpResponse(template.render(context, request))


def index(request):
    return _inner_view(request, 'index.html')


def posts(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .order_by('-published_date')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def books(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.BOOKS) \
            .order_by('-published_date')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def programming(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.PROGRAMMING) \
            .order_by('-published_date')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def travel(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.TRAVEL) \
            .order_by('-published_date')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def details(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    context = {
        'post': post,
        'category': post.category,
        'books': models.BOOKS,
        'programming': models.PROGRAMMING,
        'travel': models.TRAVEL
    }
    return _inner_view(request, 'details.html', context)
