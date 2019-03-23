from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views import generic

from . import models


def _inner_view(request, name, context={}):
    template = loader.get_template(name)
    return HttpResponse(template.render(context, request))


def index(request):
    featured = models.Post.objects \
               .filter(enabled=True) \
               .filter(featured=True) \
               .order_by('-id')
    context = {
        'featured': featured[:2],
        'books': models.Category.BOOKS.value,
        'programming': models.Category.PROGRAMMING.value,
        'travel': models.Category.TRAVEL.value
    }
    return _inner_view(request, 'index.html', context)


def posts(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .order_by('-id')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def books(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.Category.BOOKS.value) \
            .order_by('-id')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def programming(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.Category.PROGRAMMING.value) \
            .order_by('-id')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def travel(request):
    posts = models.Post.objects \
            .filter(enabled=True) \
            .filter(category=models.TRAVEL.value) \
            .order_by('-id')
    context = {'posts': posts}
    return _inner_view(request, 'posts.html', context)


def details(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    context = {
        'post': post,
        'category': post.category,
        'books': models.Category.BOOKS.value,
        'programming': models.Category.PROGRAMMING.value,
        'travel': models.Category.TRAVEL.value
    }
    return _inner_view(request, 'details.html', context)
