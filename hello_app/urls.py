# my_django_app/hello_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
