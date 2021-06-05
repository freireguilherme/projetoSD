from django.contrib import admin
from .models import Livro, InstanciaLivro, Pedido, OrdemDeEntrega

# Register your models here.
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'quantidade', 'genero', 'ano')



admin.site.register(Livro, LivroAdmin)
admin.site.register(InstanciaLivro)
admin.site.register(Pedido)
admin.site.register(OrdemDeEntrega)