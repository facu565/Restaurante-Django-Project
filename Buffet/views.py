from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate
from django.shortcuts import redirect


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
    #Sistema de Autentificacion
    user = request.user.is_authenticated
    if user == False :
        return redirect('/login/')

    cant_personas = request.POST.get('cant_p')
    date_reserva = request.POST.get('date_r')
    hora_reserva = request.POST.get('hora')

    mesas_existentes = Mesa.objects.filter(cantSillas=cant_personas)
    mesas_disponibles = []
    for t in mesas_existentes:
        mesita = t.num_Mesa
        mesas_disponibles.append(mesita)

    reserva_existentes = Reserva.objects.filter(fecha=date_reserva, hora=hora_reserva)
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
    return render(request, "reserva.html", context)


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



class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
'''
    def get(self, request):
        user = request.user.is_authenticated
        print("nel ")
        if user == False:
            return redirect('/login/')
        else:
            return render(self.request, 'home-page.html')
'''


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object' : order 
            }
            return render(self.request, 'order_summary.html', context )
        except ObjectDoesNotExist:
            messages.error(self.request, "No hay una orden activa")
            return redirect("/")



class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item=item).exists():
            order_item.quantity +=1
            order_item.save()
            messages.success(request, "Se aumento la cantidad de este producto")
        else:
            order.items.add(order_item)
            messages.success(request, "Producto agregado al carrito exitosamente")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date= ordered_date)
        order.items.add(order_item)
        messages.success(request, "Producto agregado al carrito exitosamente")
    return redirect("Buffet:product", slug=slug)

@login_required
def remove_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print("hola")
        if order.items.filter(item=item).exists():
            orderItem = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(item)
            order.save()
            messages.info(request, "Producto fue removido del carrito exitosamente")
            return redirect("Buffet:product", slug=slug)
        else:
            messages.info(request, "Este produco ya no esta en el carrito")
            return redirect("Buffet:product", slug=slug)
    else:
        messages.info(request, "Todavia no agregaste nada al carrito")
        return redirect("Buffet:product", slug=slug)
    



