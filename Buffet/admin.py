from django.contrib import admin
from.models import *

# Register your models here.
class MesaAdmin(admin.ModelAdmin):
    list_display= ['num_Mesa' , 'cantSillas']
    list_filter= ['num_Mesa' , 'cantSillas']
    search_fields= ['num_Mesa',]

admin.site.register(Mesa, MesaAdmin)