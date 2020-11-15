from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home_page(request):
    return render(request, "index.html")


def menu(request):
    return render(request,"menu.html")


def navbar(request):
    return render(request, "navbar,html")