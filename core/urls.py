from django.urls import path

from . import apps
from . import views


app_name = apps.CoreConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('books/', views.books, name='books'),
    path('programming/', views.programming, name='programming'),
    path('travel/', views.travel, name='travel'),
    path('posts/<int:post_id>/', views.details, name='details'),
]
