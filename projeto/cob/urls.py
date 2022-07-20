from django.urls import path

from cob.views import home, atletas, competicao


urlpatterns = [
    path('', home),
    path('atletas/', atletas),
    path('competicao', competicao),
]
