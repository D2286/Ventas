from django.contrib import admin

# Register your models here.
from Modulos.miregistro.models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["idC", "Nombre", "fecha_r"]

class PedidoAdmin(admin.ModelAdmin):
    list_filter = ["fecha_p"]
    list_display = ["id", "id_C", "Precio", "Efectivo", "Devolucion", "fecha_p"]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)