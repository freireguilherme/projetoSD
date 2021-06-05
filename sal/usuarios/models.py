from django.db import models
from cpf_field.models import CPFField


# Create your models here.
class Cliente(models.Model):
  cpf = CPFField('cpf')
  nome = models.CharField(max_length=200)
  senha = models.CharField(max_length=50)
  email = models.EmailField()
  cep = models.CharField(max_length=9)
  rua = models.CharField(max_length=200)
  bairro = models.CharField(max_length=200)
  
  def __str__(self):
    return self.nome