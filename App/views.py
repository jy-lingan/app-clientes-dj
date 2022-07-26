from django.shortcuts import render



# Funcion para renderizar la vista principal de la aplicación
def frontend(request):
    return render(request, 'index.html')


# Funcion para renderizar la vista backend de la aplicación
def backend(request):
    return render(request, 'backend.html')
