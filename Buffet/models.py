from django.db import models

# Create your models here.

ESTADO_MESA = [
    ('LB', 'Libre'),
    ('RS', 'Reservada'),
    ('OP', 'Ocupada'),
    ('NO', 'No Disponible'),
]

class Mesa(models.Model):
    num_Mesa = models.AutoField(primary_key=True)
    cantSillas = models.IntegerField(max_length=6)
    status = models.CharField(max_length=2, choices=ESTADO_MESA, default='Libre')

    def __str__(self):
        return 'Mesa: {}'.format(self.num_Mesa)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)

    def __str__(self):
        return self.dni


class Reserva(models.Model):
    num_Res = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Pedido(models.Model):
    num_ped = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    num_trj = models.CharField(max_length=20)
    fechaV = models.DateField()
    codSeg = models.CharField(max_length=5)

    def __str__(self):
        return self.cliente


class Bebida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Platillo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Acompaniante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre