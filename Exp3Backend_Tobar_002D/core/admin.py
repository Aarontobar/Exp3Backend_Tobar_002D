from django.contrib import admin
from .models import customer, tarjeta, producto, Orden, OrdenItem, direccion

# Register your models here.

admin.site.register(customer)
admin.site.register(tarjeta)
admin.site.register(producto)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(direccion)