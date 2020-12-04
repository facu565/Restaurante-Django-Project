from django.db import models
#import qrcode
from io import BytesIO
from django.core.files import File  
#from PIL import Image, ImageDraw
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

ESTADO_MESA = [
    ('LB', 'Libre'),
    ('RS', 'Reservada'),
    ('OP', 'Ocupada'),
    ('NO', 'No Disponible'),
]

class Mesa(models.Model):
    num_Mesa = models.AutoField(primary_key=True)
    cantSillas = models.IntegerField()
    status = models.CharField(max_length=2, choices=ESTADO_MESA, default='Libre')

    def __str__(self):
        return 'Mesa: {}'.format(self.num_Mesa)


#class Website(models.Model):
 #   name = models.CharField(max_length=200)
  #  qr_code = models.ImageField(upload_to='qr', blank=True)
#
 #   def __str__(self):
  #      return str(self.name)
#
 #   def save(self, *args, **kwargs):
  #      qrcode_img = qrcode.make(self.name)
   #     canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
    #    draw = ImageDraw.Draw(canvas)
     #   canvas.paste(qrcode_img)
      #  fname = f'qr_code-{self.name}'+'.png'
       # buffer = BytesIO()
        #canvas.save(buffer,'PNG')
        #self.qr_code.save(fname, File(buffer), save= False)
        #canvas.close()
        #super().save(*args, **kwargs)



'''
class Cliente(models.Model):
    telefono = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    correo = models.CharField(max_length=40)

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)
'''

class Reserva(models.Model):
    num_Res = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, default=2)
    fecha = models.DateField()
    hora = models.TimeField(default=datetime.now)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

'''
class Pedido(models.Model):
    num_ped = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Pago(models.Model):
    cod_pago = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    num_trj = models.CharField(max_length=20)
    fechaV = models.DateField()
    codSeg = models.CharField(max_length=5)

    def __str__(self):
        return "{}".format(self.cliente)


class Bebida(models.Model):
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Platillo(models.Model):
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Acompaniante(models.Model):
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
'''

CATEGORY_CHOICES = [
    ('CR', 'Carne Roja'),
    ('CB', 'Carne Blanca'),
    ('P', 'Pasta'),
    ('G', 'Gaseosa'),
    ('CH', 'Con Alcohol'),
    ('SG', 'Sin Gas'),



]
    

    

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    descripcion = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Buffet:product", kwargs={
            'slug': self.slug
        })

    def add_to_cart_url(self):
        return reverse("Buffet:add_to_cart", kwargs={
            'slug': self.slug
        })
        
    def get_remove_cart(self):
        return reverse("Buffet:remove_cart", kwargs={
            'slug': self.slug
        })
        


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)   
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default= False)



    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def precio_total(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default= False)

    def __str__(self):
        return self.user.username