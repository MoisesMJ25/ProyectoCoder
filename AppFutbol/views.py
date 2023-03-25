from django.shortcuts import render
from django.http import HttpResponse
from AppFutbol.models import Equipo, Jugadores, Profesores

# Create your views here.

def home(request):
    return render(request, "base.html")

def guardar_equipo(request, nombre, categoria):
    save_equipo = Equipo(nombre=nombre, categoria=categoria)
    save_equipo.save()
    context = {
        "nombre": nombre,
        "categoria": categoria
    }
    return render(request, "AppFutbol/save_equipo.html", context)


def equipos(request):
    all_equipos = Equipo.objects.all()
    contextt = {
        "cursos":all_equipos
    }
    return render(request, "AppFutbol/equipos.html")

def jugadores(request):
    all_jugadores = Jugadores.objects.all()
    contextt = {
        "Jugadores": all_jugadores
    }
    return render(request, "AppFutbol/jugadores.html")

def profesores(request):
    all_profesores = Profesores.objects.all()
    contextt = {
        "Profesores": all_profesores
    }
    return render(request, "AppFutbol/profesores.html")