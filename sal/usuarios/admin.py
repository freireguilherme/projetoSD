from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteListAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'email', 'cep')

admin.site.register(Cliente, ClienteListAdmin)


