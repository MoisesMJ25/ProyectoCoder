from django.shortcuts import render
from django.http import HttpResponse
from AppFutbol.models import Equipo

# Create your views here.
def guardar_equipo(request, nombre, categoria):
    save_equipo = Equipo(nombre="Junior", categoria="sub10")
    save_equipo.save()
    context = {
        "nombre": nombre,
        "categoría": categoria
    }
    return render(request, "AppsFutbol/save_equipo.html", context)
    #return HttpResponse (f"Equipo {equipo} creado exitosamente!")


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