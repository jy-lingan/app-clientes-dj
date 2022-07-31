from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App.models import Cliente
from django.contrib import messages
from django.http import HttpResponseRedirect
# Funcion para renderizar la vista principal de la aplicación


def frontend(request):
    return render(request, 'index.html')


# Funcion para renderizar la vista backend de la aplicación
@login_required(login_url='login')
def backend(request):
    return render(request, 'backend.html')


# Funcion para renderizar la vista agregar_cliente de la aplicación
@login_required(login_url='login')
def agregar_cliente(request):
    return render(request, 'add.html')


# Funcion para insertar un nuevo cliente en la base de datos
@login_required(login_url='login')
def agregar_cliente(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            cliente = Cliente()
            cliente.name = request.POST.get('name')
            cliente.phone = request.POST.get('phone')
            cliente.email = request.POST.get('email')
            cliente.age = request.POST.get('age')
            cliente.gender = request.POST.get('gender')
            cliente.note = request.POST.get('note')
            cliente.save()
            messages.success(request, 'Cliente agregado correctamente')
            return HttpResponseRedirect('/backend')
    else:
        messages.error(request, 'Faltan datos')
        return render(request, 'add.html')
