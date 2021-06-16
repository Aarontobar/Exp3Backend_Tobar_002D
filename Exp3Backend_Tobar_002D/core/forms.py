from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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