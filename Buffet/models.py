from django.db import models

# Create your models here.

class Mesa(models.Model):
    num_Mesa = models.AutoField(primary_key=True)
    cantSillas = models.IntegerField(max_length=6)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)

class Reserva(models.Model):
    num_Res = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

