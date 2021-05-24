from . import models
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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