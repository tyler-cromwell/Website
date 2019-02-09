from django.urls import path

from . import apps
from . import views


app_name = apps.CoreConfig.name

urlpatterns = [
    path('', views.index, name='index'),
]
