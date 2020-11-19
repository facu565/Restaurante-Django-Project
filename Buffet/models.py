from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File  
from PIL import Image, ImageDraw

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


class Website(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save= False)
        canvas.close()
        super().save(*args, **kwargs)


class Cliente(models.Model):
    telefono = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    correo = models.CharField(max_length=40)

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)


class Reserva(models.Model):
    num_Res = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


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