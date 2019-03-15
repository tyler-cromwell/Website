from django.urls import path

from . import apps
from . import views


app_name = apps.CoreConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.details, name='details'),
    path('blog/', views.blog, name='blog'),
]
