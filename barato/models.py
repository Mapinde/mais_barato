from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=128)
    localizacao = models.CharField(max_length=128)
    logo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=10)
    email = models.EmailField()
    data_criacao = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nome

class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nome_long = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    preco = models.CharField(max_length=20)
    imagem = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nome_long