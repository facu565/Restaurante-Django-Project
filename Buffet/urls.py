from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from Buffet import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'Buffet'

urlpatterns = [
    path('', home_page),
    path('menu/', menu),
    path('nav/', navbar),
    path('reserva/', reserva),
    path('register/', register),
    path('login/', LoginView.as_view(template_name = 'login.html')),
    path('logout/', LogoutView.as_view(template_name = 'logout.html')),
    path('producto/<slug>/', ItemDetailView.as_view(), name = 'product'),
    path('order_summary/', OrderSummaryView.as_view(), name = 'order_summary'),
    path('grilla/', HomeView.as_view()),
    path('add_to_cart/<slug>/', add_to_cart, name = 'add_to_cart'),
    path('remove-cart/<slug>/', remove_cart, name = 'remove-cart')


    


]