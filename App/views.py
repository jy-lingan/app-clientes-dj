from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Funcion para renderizar la vista principal de la aplicación
def frontend(request):
    return render(request, 'index.html')


# Funcion para renderizar la vista backend de la aplicación
@login_required(login_url='login')
def backend(request):
    return render(request, 'backend.html')
