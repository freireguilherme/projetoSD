from django.contrib import admin
from aluguel.models import Cliente, Livro, InstanciaLivro, Pedido, OrdemDeEntrega

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Livro)
admin.site.register(InstanciaLivro)
admin.site.register(Pedido)
admin.site.register(OrdemDeEntrega)