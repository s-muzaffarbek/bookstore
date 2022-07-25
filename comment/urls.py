from django.contrib import admin
from django.urls import path
from .views import liked

urlpatterns = [
    path('like/', liked, name='like'),
]