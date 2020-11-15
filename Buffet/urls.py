from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from Buffet import views

urlpatterns = [
    path('', home_page),
    path('menu/', menu),
    path('nav/', menu),

]