# my_django_app/hello_app/admin.py
from django.contrib import admin
from .models import Message

admin.site.register(Message)
