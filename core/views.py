from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views import generic

from . import models


def _inner_view(request, name, context={}):
    context.update({
        'books': models.Category.BOOKS.value,
        'programming': models.Category.PROGRAMMING.value,
        'travel': models.Category.TRAVEL.value
    })
    template = loader.get_template(name)
    return HttpResponse(template.render(context, request))


def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-id')
    context = {'posts': posts}
    return _inner_view(request, 'index.html', context)


def details(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    images = models.Image.objects.filter(post=post_id).order_by('order')
    code = models.Code.objects.filter(post=post_id).order_by('order')
    #related = models.Post.objects.filter(enabled=True).order_by('-id')
    context = {
        'post': post,
        'images': images,
        'code': code
        #'related': related
    }
    return _inner_view(request, post.path, context)
