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
    user_name = request.user.id
    print(date_reserva, cant_personas, hora_reserva, user_name)
    mesas_existentes = Mesa.objects.filter(cantSillas=cant_personas)
    mesas_disponibles = []
    for t in mesas_existentes:
        mesita = t.num_Mesa
        mesas_disponibles.append(mesita)
    print(mesas_disponibles)
    reserva_existentes = Reserva.objects.filter(fecha = date_reserva, hora = hora_reserva)
    reserva_disponible = []
    for t in reserva_existentes:
        reservita = t.num_Res
        reserva_disponible.append(reservita)
    print(reserva_disponible)
    print("no es aca el problema 1")
    for i in mesas_disponibles:
        print("no es aca el problema 2")
        for j in reserva_disponible:
            print("no es aca el problema 3")
            if (i == j):
                print("no")
            else:
                print(i)
                la_mesa = Mesa.objects.get(num_Mesa=i)
                Reserva.objects.create(fecha=date_reserva, hora=hora_reserva, mesa=la_mesa, cliente=user_name)
                print("si")

    #Reserva.objects.create(fecha=date_reserva,hora=hora_reserva,mesa=)
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
