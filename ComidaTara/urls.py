from django.urls import path
from .views import *
from .urls import *

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('entrada/', entrada, name= 'entrada'),
    path('principal/', principal, name= 'principal'),
    path('postre/', postre, name= 'postre'),
    #path('buscarentradas/', buscarentrada, name='BuscarEntrada'),
    path('busquedaEntrada/', busquedaEntrada, name= 'busquedaEntrada'),
    path('buscar/', buscar, name='buscar'),
    path('buscarPrincipal/', buscarPrincipal, name='buscarPrincipal'),
    path('buscarPostre/', buscarPostre, name='buscarPostre'),
    ]
   