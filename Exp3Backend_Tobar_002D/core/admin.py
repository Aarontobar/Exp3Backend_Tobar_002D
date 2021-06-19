from django.contrib import admin
from .models import cliente, producto, Orden, OrdenItem, direccion

# Register your models here.

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(direccion)