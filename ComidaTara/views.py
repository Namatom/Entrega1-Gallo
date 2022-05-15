
from django.http import HttpResponse
from django.shortcuts import render

from ComidaTara.forms import *
from ComidaTara import *
from .models import *
# Create your views here.

def inicio(request):
    return render(request, "ComidaTara/inicio.html")

def entrada(request):

    if request.method == 'POST':
        formulario=EntradaForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            entrada= Entrada(nombre=informacion['nombre'], descripcion=informacion['descripcion'], precio=informacion['precio'] )
            entrada.save()
            return render(request, "ComidaTara/inicio.html")
    else:
        formulario=EntradaForm()
        return render(request, "ComidaTara/entradas.html", {'formulario':formulario})

def principal(request):

    if request.method == 'POST':
        formulario=PrincipalForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            principal= Principal(nombre=informacion['nombre'], descripcion=informacion['descripcion'], precio=informacion['precio'] )
            principal.save()
            return render(request, "ComidaTara/inicio.html")
    else:
        formulario=PrincipalForm()
        return render(request, "ComidaTara/principales.html", {'formulario': formulario})

def postre(request):
    if request.method == 'POST':
        formulario=PostreForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            postre= Postre(nombre=informacion['nombre'], descripcion=informacion['descripcion'], precio=informacion['precio'] )
            postre.save()
            return render(request, "ComidaTara/inicio.html")
    else:
        formulario=PostreForm()
        return render(request, "ComidaTara/postres.html", {'formulario': formulario})
    return render(request, "ComidaTara/postres.html")


'''def buscarentrada(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        entrada=Entrada.objects.filter(nombre=nombre)
        return render(request, "ComidaTara/resultados.html",{'entrada':entrada})
    else:
        respuesta="No se ingreso ninguna entrada"
        return render(request, "ComidaTara/inicio.html", {"respuesta":respuesta})'''

def busquedaEntrada(request):
    return render(request, "ComidaTara/busquedaEntrada.html")

def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        entradas=Entrada.objects.filter(nombre__icontains=nombre)
        return render(request, 'ComidaTara/resultados.html', {'entradas':entradas})
    else:
        respuesta="No se ingreso nada"
        return render(request, "ComidaTara/entradas.html", {'respuesta':respuesta})

def buscarPrincipal(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        principales=Principal.objects.filter(nombre__icontains=nombre)
        return render(request, 'ComidaTara/resultadosPrincipales.html', {'principales':principales})
    else:
        respuesta="No se ingreso nada"
        return render(request, "ComidaTara/principales.html", {'respuesta':respuesta})

def buscarPostre(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        postres=Postre.objects.filter(nombre__icontains=nombre)
        return render(request, 'ComidaTara/resultadosPostres.html', {'postres':postres})
    else:
        respuesta="No se ingreso nada"
        return render(request, "ComidaTara/postres.html", {'respuesta':respuesta})