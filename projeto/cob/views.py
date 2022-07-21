from django.shortcuts import render


def home(request):
    return render(request, 'cob/pages/home.html', context={'name': 'Gabriel Vidal'})

