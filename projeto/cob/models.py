from platform import mac_ver
from unicodedata import name

from django.db import models


class Competicao(models.Model):
    nome = models.CharField(max_length=65)
    data = models.DateField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Atletas(models.Model):
    nome = models.CharField(max_length=65)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    competicao = models.ForeignKey(Competicao, on_delete=models.SET_NULL, null=True)
