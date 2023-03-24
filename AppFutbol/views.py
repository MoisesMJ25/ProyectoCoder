from django.shortcuts import render
from django.http import HttpResponse
from AppFutbol.models import Equipo

# Create your views here.
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
    pass

def profesores(request):
    pass