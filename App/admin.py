from django.contrib import admin
from App.models import Cliente

# Registramos el modelo Cliente en el admin
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender','created_at']
    search_fields = ['name', 'phone', 'email', 'gender']
    list_per_page = 8
    
admin.site.register(Cliente, ClienteAdmin)
