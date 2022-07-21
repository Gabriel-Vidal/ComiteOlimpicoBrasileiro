from django.shortcuts import render


def home(request):
    return render(request, 'cob/home.html', context={'name': 'Gabriel Vidal,'})

