from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from Buffet import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_page),
    path('menu/', menu),
    path('nav/', navbar),
    path('register/', register),
    path('login/', LoginView.as_view(template_name = 'login.html')),
    path('logout/', LogoutView.as_view(template_name = 'logout.html')),


    


]