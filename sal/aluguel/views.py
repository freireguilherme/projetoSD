from . import models
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

  num_instancias = models.InstanciaLivro.objects.all().count()

  context = {
    'num_instancias': num_instancias,
    }
  return render(request, 'index.html', context=context)