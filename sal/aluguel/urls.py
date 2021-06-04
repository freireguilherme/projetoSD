from django.urls import path
from .views import *

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('cadastrar/cliente', ClienteCreate.as_view(), name='cadastrar-cliente'),
  path('cadastrar/livro', LivroCreate.as_view(), name='cadastrar-livro'),
  path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar-livro'),
  path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
  path('listar/livros', LivroList.as_view(), name='listar-livros'),
]
