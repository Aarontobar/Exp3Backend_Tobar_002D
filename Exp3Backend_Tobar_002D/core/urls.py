from django.urls import path
from .views import inicio, nosotros, galeria, registro, inicio_sesion, comprar, api

urlpatterns = [
    path ('', inicio, name="inicio"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('galeria/', galeria, name="galeria"),
    path ('registro/' ,registro, name="registro"),
    path ('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path ('comprar/', comprar, name="comprar"),
    path ('api/', api, name="api")
]