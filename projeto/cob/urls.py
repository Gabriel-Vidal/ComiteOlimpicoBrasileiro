from django.urls import path

from cob.views import home


urlpatterns = [
    path('', home),   
]
