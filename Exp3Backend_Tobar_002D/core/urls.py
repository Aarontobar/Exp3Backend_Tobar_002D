from django.urls import path
from .views import inicio, nosotros, galeria, registro, inicio_sesion, comprar, api

urlpatterns = [
    path ('', inicio, name="inicio"),
    path ('request' ,nosotros, name="nosotros"),
    path ('request1' ,galeria, name="galeria"),
    path ('request2', registro, name="registro"),
    path ('request3', inicio_sesion, name="inicio_sesion"),
    path ('request4', comprar, name="comprar"),
    path ('request5', api, name="api")
]