from django.urls import path

from . import views

app_name = 'COB'

urlpatterns = [
    path('', views.home, name="home"),
    path('cob/<int:id>/', views.cob, name="evento"),
]
