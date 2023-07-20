from django.urls import path, include
from django.contrib import admin
from .views import index, go_back


urlpatterns = [

    path('', index),
    path('go back/', go_back)
]