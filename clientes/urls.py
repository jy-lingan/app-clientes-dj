"""clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Path del admin de Django
    path('admin/', admin.site.urls),
    # Path del render principal de la aplicación
    path('', views.frontend, name='frontend'),
    # Path Login/Logout
    path('login/', include('django.contrib.auth.urls')),

    # Backend de la aplicación
    # Path de acceso al backends

    path('backend/', views.backend, name='backend'),
    # Path de agregar clientes
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),

]
