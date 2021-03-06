from django.urls import path, include
from .views import inicio, nosotros, galeria, registro, inicio_sesion, api, form_cuenta, carrito, updateItem, compra, ordenar, usuario, eliminar, crearProducto, modificarProducto

urlpatterns = [
    path ('inicio/', inicio, name="inicio"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('galeria/', galeria, name="galeria"),
    path ('registro/' ,registro, name="registro"),
    path ('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path ('api/', api, name="api"),
    path ('form_cuenta', form_cuenta, name="form_cuenta"),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('carrito/', carrito, name="carrito"),
    path ('update_item/', updateItem, name="update_item"),
    path ('compra/', compra, name="compra"),
    path ('ordenar/', ordenar, name="ordenar"),
    path ('usuario/', usuario, name="usuario"),
    path ('eliminar/<id>', eliminar, name="eliminar"),
    path ('crearProducto/', crearProducto, name="crearProducto"),
    path ('modificarProducto/<id>', modificarProducto, name="modificarProducto")
]