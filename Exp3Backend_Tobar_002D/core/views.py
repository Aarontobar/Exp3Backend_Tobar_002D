from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def galeria(request):
    return render(request, 'galeria.html')

def registro(request):
    return render(request, 'registro.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def comprar(request):
    return render(request, 'comprar.html')

def api(request):
    return render(request, 'api.html')