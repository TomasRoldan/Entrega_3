from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .forms import *
from .models import *

def indice(request):
    return render(request, 'App_TP3/index.html')

def camisetas(request):
    return render(request,'App_TP3/camisetas.html')

def pantalones(request):
    return render(request,'App_TP3/pantalones.html')

def abrigos(request):
    return render(request,'App_TP3/abrigos.html')


def camiseta_form(request):

    if request.method == "POST":

        miCamiseta = CamisetaForm(request.POST)

        if miCamiseta.is_valid():
            info = miCamiseta.cleaned_data
            camiseta = Camiseta(equipo=info["equipo"], año=info["año"], equipación=info["equipación"], talle=info["talle"], precio=info["precio"])
            camiseta.save()
            return render(request, 'App_TP3/index.html')
    else:
        miCamiseta =CamisetaForm()

    return render(request, "App_tp3/camisetas.html", {"miCamiseta":miCamiseta})    

def pantalon_form(request):

    if request.method == "POST":

        miPantalon = PantalonForm(request.POST)

        if miPantalon.is_valid():
            info = miPantalon.cleaned_data
            pantalon = Pantalon(equipo=info["equipo"], año=info["año"], equipación=info["equipación"], modelo=info["modelo"], talle=info["talle"], precio=info["precio"])
            pantalon.save()
            return render(request, 'App_TP3/index.html')
    else:
        miPantalon =PantalonForm()

    return render(request, "App_tp3/pantalon.html", {"miPantalon":miPantalon})   


def abrigo_form(request):

    if request.method == "POST":

        miAbrigo = AbrigoForm(request.POST)

        if miAbrigo.is_valid():
            info = miAbrigo.cleaned_data
            abrigo = Abrigo(equipo=info["equipo"], año=info["año"], modelo=info["modelo"], talle=info["talle"], precio=info["precio"])
            abrigo.save()
            return render(request, 'App_TP3/index.html')
    else:
        miAbrigo =AbrigoForm()

    return render(request, "App_tp3/abrigo.html", {"miAbrigo":miAbrigo})  


def buscar_camiseta(request):
    if request.method == "POST":
        buscar_camiseta = BuscarCamisetaForm(request.POST)

        if buscar_camiseta.is_valid():
            info = buscar_camiseta.cleaned_data
            camisetas = Camiseta.objects.filter(equipo=info["equipo"])
            return render(request, "App_TP3/lista_camisetas.html", {"camisetas": camisetas})
    else:
        buscar_camiseta = BuscarCamisetaForm()
        return render(request, "App_TP3/buscar_camiseta.html", {"miCamiseta": buscar_camiseta})