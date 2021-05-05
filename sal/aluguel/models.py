import datetime
import uuid
from django.db import models
from django.utils import timezone

# Create your models here.

#salva informações sobre clientes
class Cliente(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  cpf = models.IntegerField()
  nome = models.CharField(max_length=200)
  senha = models.CharField(max_length=8)
  email = models.EmailField()
  cep = models.IntegerField(),
  rua = models.CharField(max_length=200),
  bairro = models.CharField(max_length=200),
  
  def __str__(self):
    return self.nome

#salva informações gerais sobre a biblioteca 
class Livro(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=200)
  #numero de livros do estoque
  quantidade = models.IntegerField()
  genero = models.CharField(max_length=200)
  ano = models.IntegerField()

  def __str__(self):
    return self.nome

#informações sobre um livro específico 
class InstanciaLivro(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  livro = models.ForeignKey(Livro, on_delete = models.SET_NULL, null = True)
  devolucao = models.DateField()

  STATUS_EMPRESTIMO = (
    ('m', 'Manutenção'),
    ('e', 'Emprestado'),
    ('d', 'Disponível'),
    ('r', 'Reservado'),
  )

  status = models.CharField(
    max_length=1,
    choices=STATUS_EMPRESTIMO,
    blank = True,
    default = 'm',
    help_text = 'Disponibilidade do livro',
  )

#salva informações sobre o pedido de um cliente
class Pedido(models.Model):
  #codigo do pedido
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  #qual cliente fez o pedido
  cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
  #o cliente pediu qual livro
  livro = models.ForeignKey(Livro, on_delete = models.CASCADE)
  #data do pedido
  dataPedido = models.DateTimeField(auto_now_add=True, blank=True)
  #data da devolução
  def data_devolucao(self):
    return dataPedido + datetime.timedelta(days=30)
  #valor do pedido
  valor = models.CharField(max_length=100)

  def __str__(self):
    return self.codigoPedido

#salva informações sobre a entrega do pedido
class OrdemDeEntrega(models.Model):
  #codigo da entrega (ratreamento?)
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  #entrega do pedido. uma entrega se relaciona com um pedido e vice-versa
  pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
  
  def dataEntrega():
    return pedido.dataPedido + datetime.timedelta(days=1)

  def __str__(self):
    return self.codigo