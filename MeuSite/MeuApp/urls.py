rom django.urls import path
from MeuApp import views

urlpatterns = [
    path('', MeuApp.home, name='homepage'),
    path('SegundaPagina',
        MeuApp.segundaPagina, name='segunda'),
]