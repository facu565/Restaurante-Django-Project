from django.contrib import admin
from.models import *

# Register your models here.
#class ClienteInline(admin.TabularInline):
#    model= Cliente

'''
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido']
    list_filter= ['id', 'nombre', 'apellido']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido', 'dni',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        })
    )
'''
class ReservaAdmin(admin.ModelAdmin):
    #inline= [ClienteInline]
    list_display= ['num_Res', 'fecha', 'cliente', 'hora', 'mesa']
    fieldsets = (
        ("Fecha de Reserva", {
            'fields': ('fecha','hora')
        }),
        ('Datos de la Reserva', {
            'fields': ('cliente','mesa')
        })
    )
'''
class PedidoAdmin(admin.ModelAdmin):
    inline= [ClienteInline]
    list_display= ['num_ped', 'cliente',]
'''
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'slug', 'descripcion', ]
    fieldsets = (
        ("Informacion Principal", {
            'fields': ('title', 'price', 'category')
        }),
        ('Detalles', {
            'fields': ('slug', 'descripcion')
        })
    )

'''class PagoAdmin(admin.ModelAdmin):
    inline=[ClienteInline]
    list_display= [ 'cliente' ,'num_trj', 'fechaV', 'codSeg',]
    fieldsets = (
        ("Datos Personales", {
            'fields': ( 'cliente',)
        }),
        ('Forma de pago', {
            'fields': ('num_trj', 'fechaV', 'codSeg',)
        })
    )
'''

#class WebsiteAdmin(admin.ModelAdmin):
    #list_display = ['name', 'qr_code', ]


class MesaAdmin(admin.ModelAdmin):
    list_display= ['num_Mesa' , 'cantSillas']
    list_filter= ['num_Mesa' , 'cantSillas']
    search_fields= ['num_Mesa',]

'''
class BebidaAdmin(admin.ModelAdmin):
    list_display= ['id', 'nombre']


class PlatilloAdmin(admin.ModelAdmin):
    list_display= ['id', 'nombre']


class AcompanianteAdmin(admin.ModelAdmin):
    list_display= ['id', 'nombre']
'''





admin.site.register(Mesa, MesaAdmin)
admin.site.register(Reserva, ReservaAdmin)
#admin.site.register(Cliente, ClienteAdmin)
#admin.site.register(Pedido, PedidoAdmin)
#admin.site.register(Pago, PagoAdmin)
#admin.site.register(Bebida, BebidaAdmin)
#admin.site.register(Platillo, PlatilloAdmin)
#admin.site.register(Acompaniante, AcompanianteAdmin)
#admin.site.register(Website, WebsiteAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)