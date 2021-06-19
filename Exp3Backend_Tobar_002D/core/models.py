from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class producto(models.Model):
    nombre= models.CharField(max_length=50, verbose_name='nombre', null=True)
    precio= models.IntegerField(verbose_name='precio')
    descripcion= models.CharField(max_length=500, verbose_name='descripcion', null=True)
    foto= models.ImageField(verbose_name='foto')

    def __str__(self):
        return(self.nombre)

    @property
    def fotoURL(self):
        try:
            url = self.foto.url
        except:
            url = ''
        return url

class Orden(models.Model):
    cliente= models.ForeignKey(cliente, on_delete=models.CASCADE, null=True)
    fecha_orden= models.DateTimeField(auto_now_add=True)
    completo= models.BooleanField(default=False, null=True, blank=False)
    transaccion_id= models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def envio(self):
        envio = True
        return envio

    @property
    def getTotalCarrito(self):
        ordenitems = self.ordenitem_set.all()
        total = sum([item.get_total for item in ordenitems])
        return total

    @property
    def getItemsCarrito(self):
        ordenitems = self.ordenitem_set.all()
        total = sum([item.cantidad for item in ordenitems])
        return total


class OrdenItem(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

class direccion(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    codigopostal = models.CharField(max_length=200, null=True)
    fecha_annadido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)