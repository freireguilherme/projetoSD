from django.db import models

# Create your models here.
class Cliente(models.Model):
  cpf = models.IntegerField()
  nome = models.CharField(max_length=200)
  senha = models.CharField(max_length=8)
  email = models.EmailField()
  cep = models.IntegerField()
  rua = models.CharField(max_length=200)
  bairro = models.CharField(max_length=200)
  
  def __str__(self):
    return self.nome