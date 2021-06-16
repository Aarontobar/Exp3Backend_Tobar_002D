from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.contrib.auth.models import Group
from .models import *

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        try:
            request.user.customer
        except ObjectDoesNotExist:
            customer.objects.create(
                user= request.user,
                name= request.user.first_name,
                email= request.user.email,
            )
        custom = request.user.customer
        orden, created = Orden.objects.get_or_create(customer=custom, completo=False)
        items = orden.ordenitem_set.all()
        carritoItems = orden.getItemsCarrito
    else:
        items = []
        orden = {'getItemsCarrito':0, 'getTotalCarrito':0}
        carritoItems = orden['getItemsCarrito']

    productos= producto.objects.all()
    context = {'productos':productos, 'carritoItems':carritoItems}
    return render(request, 'inicio.html', context)

def nosotros(request):
    return render(request, 'nosotros.html')

def galeria(request):
    return render(request, 'galeria.html')

def registro(request):
    return render(request, 'registro.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def api(request):
    return render(request, 'api.html')

def form_cuenta(request):

    if request.method=='POST':
        cuenta_form = cuentaForm(request.POST)
        if cuenta_form.is_valid():
            user = cuenta_form.save()
            cuenta_form.save()
            grupo= Group.objects.get(name='clientes')
            user.groups.add(grupo)
            return redirect('login')
    else:
        cuenta_form=cuentaForm()
    return render(request, 'core/form_crearcuenta.html',{'cuenta_form':cuenta_form})

def carrito(request):
    customer = request.user.customer
    orden, created = Orden.objects.get_or_create(customer=customer, completo=False)
    items = orden.ordenitem_set.all()
    carritoItems = orden.getItemsCarrito
    context = {'items':items, 'orden':orden, 'carritoItems':carritoItems}
    return render(request, 'carrito.html', context)


def checkout(request):
    customer = request.user.customer
    orden, created = Orden.objects.get_or_create(customer=customer, completo=False)
    items = orden.ordenitem_set.all()

    context = {'items':items, 'orden':orden}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productoId = data['productoId']
    accion = data['accion']

    print('productoId: ', productoId, 'accion', accion)

    customer = request.user.customer
    Producto = producto.objects.get(id=productoId)
    orden, created = Orden.objects.get_or_create(customer=customer, completo=False)

    ordenItem, created = OrdenItem.objects.get_or_create(orden=orden, producto=Producto)

    if accion == 'add':
        ordenItem.cantidad = (ordenItem.cantidad + 1)
    elif accion == 'remove':
        ordenItem.cantidad = (ordenItem.cantidad - 1)
    
    ordenItem.save()

    if ordenItem.cantidad <= 0:
        ordenItem.delete()

    return JsonResponse('Item annadido', safe=False)

def ordenar(request):
    transaccion_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    orden, created = Orden.objects.get_or_create(customer=customer, completo=False)
    total = (data['total'])
    orden.transaccion_id = transaccion_id

    orden.completo = True
    orden.save()

    direccion.objects.create(
        customer=customer,
        orden=orden,
        direccion=data['envio']['direccion'],
        ciudad=data['envio']['ciudad'],
        region=data['envio']['region'],
        codigopostal=data['envio']['codigopostal']
    )
    return JsonResponse('pago completo', safe=False)

def usuario(request):
    grupos= Group.objects.get(name='clientes')
    grupo= request.user.groups.get()
    if grupo==grupos:
        cliente=True
    else:
        cliente=False
    customer = request.user.customer
    direcciones = direccion.objects.filter(customer=customer)
    productos =producto.objects.all()
    

    context= {'direcciones': direcciones, 'cliente':cliente,'productos':productos}
    return render(request, 'usuario.html',context)

def eliminar(request, id):
    productos = producto.objects.get(id=id)
    productos.delete()
    return redirect('usuario')

def crearProducto(request):

    if request.method=='POST':
        form = productoform(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form=productoform()

    return render(request, 'core/form_producto.html', {'form':form})