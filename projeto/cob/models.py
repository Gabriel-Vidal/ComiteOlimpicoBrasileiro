from platform import mac_ver

from django.db import models


class Competicao(models.Model):
    nome = models.CharField(max_length=65)
    data = models.DateField()
    descricao = models.CharField(max_length=100)


class Atletas(models.Model):
    nome = models.CharField(max_length=65)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    competicao = models.ForeignKey(Competicao, on_delete=models.SET_NULL, null=True)
