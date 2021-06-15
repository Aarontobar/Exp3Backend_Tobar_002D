from django.urls import path, include
from .views import inicio, nosotros, galeria, registro, inicio_sesion, comprar, api, form_cuenta, carrito, updateItem, checkout, ordenar

urlpatterns = [
    path ('', inicio, name="inicio"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('galeria/', galeria, name="galeria"),
    path ('registro/' ,registro, name="registro"),
    path ('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path ('comprar/', comprar, name="comprar"),
    path ('api/', api, name="api"),
    path ('form_cuenta', form_cuenta, name="form_cuenta"),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('carrito/', carrito, name="carrito"),
    path ('update_item/', updateItem, name="update_item"),
    path ('checkout/', checkout, name="checkout"),
    path ('ordenar/', ordenar, name="ordenar")
]