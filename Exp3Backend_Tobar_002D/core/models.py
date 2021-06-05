from django.db import models

# Create your models here.

class cuenta(models.Model):
    nombre= models.CharField(max_length=40, verbose_name='nombre')
    apellido= models.CharField(max_length=40, verbose_name='apellido')
    correo= models.CharField(primary_key=True, max_length=40, verbose_name='correo')
    contaseña= models.CharField(max_length=40, verbose_name='contraseña')
    mes= models.IntegerField(verbose_name='mes')
    dia= models.IntegerField(verbose_name='dia')
    anno= models.IntegerField(verbose_name='anno')

    def __str__(self):
        return(self.correo)