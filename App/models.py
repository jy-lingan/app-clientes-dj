from logging import PlaceHolder
from django.db import models

# Creamos un modelo para la tabla cliente


class Cliente(models.Model):
    GENDER = (
        ('MUJER', 'MUJER'),
        ('HOMBRE', 'HOMBRE'),
        ('OTRO', 'OTRO'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=100, help_text='Nombre del cliente', verbose_name='Nombre')
    phone = models.CharField(
        max_length=100, help_text='Telefono del cliente', verbose_name='Telefono')
    email = models.CharField(
        max_length=100, help_text='Email del cliente', verbose_name='Email')
    age = models.IntegerField(
        help_text='Edad del cliente', verbose_name='Edad')
    gender = models.CharField(
        max_length=100, null=True, choices=GENDER, verbose_name='Género')
    note = models.TextField(verbose_name='Nota')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
