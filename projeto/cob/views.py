from django.shortcuts import render


def home(request):
    return render(request, 'cob/pages/home.html', context={'name': 'Gabriel Vidal'})


def cob(request, id):
    return render(request, 'cob/pages/cob-view.html', context={'name': 'Gabriel Vidal'})