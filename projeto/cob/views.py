from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'cob/home.html')


def atletas(request):
    return HttpResponse('informe os atletas3')


def competicao(request):
    return HttpResponse('Insira as informaçoes do atleta')
