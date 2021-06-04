from .models import Livro
from usuarios.models import Cliente
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


# Create your views here.
class IndexView(TemplateView):
  template_name="index.html"
  model = Livro

  def index(request):

    num_livros = models.Livro.objects.all().count()
    num_instancias = models.InstanciaLivro.objects.all().count()
    num_instancias_disponiveis = models.InstanciaLivro.objects.filter(status__exact='d').count()
    listar_livros = models.Livro.objects.all()

    context = {
      'num_livros': num_livros,
      'num_instancias': num_instancias,
      'num_instancias_disponiveis': num_instancias_disponiveis,
      'listar_livros': listar_livros,
      }
    return render(request, 'index.html', context=context)
class ClienteCreate(CreateView):
  model = Cliente
  fields = ['cpf', 'nome', 'email', 'cep', 'bairro', 'senha']
  template_name = 'formulario.html'
  success_url = reverse_lazy('index')

class LivroCreate(CreateView):
  model = Livro
  fields = ['titulo', 'autor', 'quantidade', 'genero', 'ano']
  template_name = 'formulario.html'
  success_url = reverse_lazy('listar-livros')

class LivroUpdate(UpdateView):
  model = Livro
  fields = ['titulo', 'autor', 'quantidade', 'genero', 'ano']
  template_name = 'formulario.html'
  success_url = reverse_lazy('listar-livros')

class LivroDelete(DeleteView):
  model = Livro
  template_name = 'exclusao.html'
  success_url = reverse_lazy('listar-livros')

class LivroList(LoginRequiredMixin, ListView):
  model = Livro
  login_url = reverse_lazy('login')
  template_name = 'listar_livros.html'
"""
  def index(request):

  num_livros = models.Livro.objects.all().count()
  num_instancias = models.InstanciaLivro.objects.all().count()
  num_instancias_disponiveis = models.InstanciaLivro.objects.filter(status__exact='d').count()
  listar_livros = models.Livro.objects.all()

  context = {
    'num_livros': num_livros,
    'num_instancias': num_instancias,
    'num_instancias_disponiveis': num_instancias_disponiveis,
    'listar_livros': listar_livros,
    }
  return render(request, 'index.html', context=context)
  """