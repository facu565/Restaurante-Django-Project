from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from .models import *

# Create your views here.
def home_page(request):
    return render(request, "index.html")


def menu(request):
    obj = Website.objects.all().first()
    print(obj)
    context = {
        'img': obj,
    }
    return render(request,"menu.html", context)



def navbar(request):
    return render(request, "navbar.html")


def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, "register.html",{'form': form})

def login (request):

    return render(request, "login.html")
