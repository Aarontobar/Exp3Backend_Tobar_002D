from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class cuentaForm(UserCreationForm):

    class Meta:
        model= User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        labels ={
            'username': 'usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'email',
            'password1':'contrasenna'
        }
        widgets={
            'username': forms.TextInput(
                attrs={
                    'id': 'usuario',
                    'name': 'usuario'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'id': 'nombre',
                    'name': 'nombre'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'id': 'apellido',
                    'name': 'apellido'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'name': 'email'
                }
            )
        }

class productoform(ModelForm):

    class Meta:
        model=producto
        fields= ['nombre', 'descripcion', 'precio', 'foto',]
        labels ={
            'nombre': 'Ingrese nombre del producto',
            'stock': 'Ingrese candidad del producto disponible',
            'descripcion': 'ingrese una descripcion para este producto por favor',
            'foto': 'Seleccione foto del producto'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'id': 'nombre',
                    'name': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'id': 'descripcion',
                    'name': 'descripcion'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'id': 'precio',
                    'name': 'precio'
                }
            )
        }
