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

def reserva(request):
    cant_personas = request.POST.get('cant_p')
    date_reserva = request.POST.get('date_r')
    hora_reserva = request.POST.get('hora')
    mesas_existentes = Mesa.objects.filter(cantSillas=cant_personas)
    mesas_disponibles = []
    for t in mesas_existentes:
        mesita = t.num_Mesa
        mesas_disponibles.append(mesita)
    reserva_existentes = Reserva.objects.filter(fecha = date_reserva, hora = hora_reserva)
    reserva_disponible = []
    for m in reserva_existentes:
        reservita = m.num_Res
        reserva_disponible.append(reservita)
    if request.method == "POST":
        for i in mesas_disponibles:
            if (i in reserva_disponible):
                pass
            else:
                la_mesa = Mesa.objects.get(num_Mesa=i)
                Reserva.objects.create(fecha=date_reserva, hora=hora_reserva, mesa=la_mesa, cliente=request.user)
                break
    context = {}
    return render(request,"reserva.html", context)


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
