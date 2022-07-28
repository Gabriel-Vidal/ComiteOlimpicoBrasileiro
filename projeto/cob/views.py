from django.shortcuts import render
from util.cob.factory import make_eventos


def home(request):
    return render(request, 'cob/pages/home.html', context={
        'cobs': [make_eventos() for _ in range(5)],
        })


def cob(request, id):
    return render(request, 'cob/pages/cob-view.html', context={
        'cob': make_eventos(),
    })
