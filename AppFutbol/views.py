from django.shortcuts import render
from django.http import HttpResponse
from AppFutbol.models import Equipo

# Create your views here.
def guardar_equipo(request):
    equipo = Equipo(nombre="Junior", categoria="sub10")
    equipo.save()
    return HttpResponse (f"Equipo {equipo} creado exitosamente!")