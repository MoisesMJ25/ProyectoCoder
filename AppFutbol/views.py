from django.shortcuts import render
from django.http import HttpResponse
from AppFutbol.models import Equipo, Jugadores, Profesores
from AppFutbol.forms import EquipoForm, JugadorForm, ProfesorForm, BusquedaEquipoForm

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
    if request.method == "POST":
        mi_formulario = EquipoForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            equipo_save = Equipo(
                nombre=info['nombre'],
                categoria=info['categoria']
            )
            equipo_save.save()

    all_equipos = Equipo.objects.all()
    context = {
        "equipos": all_equipos,
        "form": EquipoForm(),
        "form_busqueda": BusquedaEquipoForm(),
    }
    return render(request, "AppFutbol/equipos.html", context=context)



def jugadores(request):
    if request.method == "POST":
        mi_formulario = JugadorForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            jugador_save = Jugadores(
                nombre=info['nombre'],
                apellido=info['apellido'],
                edad=info['edad']
            )
            jugador_save.save()

    all_jugadores = Jugadores.objects.all()
    context = {
        "jugadores": all_jugadores,
        "form": JugadorForm
    }
    return render(request, "AppFutbol/jugadores.html", context=context)



def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            profesor_save = Profesores(
                nombre=info['nombre'],
                apellido=info['apellido'],
                email=info['email']
            )
            profesor_save.save()

    all_profesores = Profesores.objects.all()
    context = {
        "profesores": all_profesores,
        "form": ProfesorForm
    }
    return render(request, "AppFutbol/profesores.html", context=context)


def busqueda_equipo(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaEquipoForm(request.GET)
    if mi_formulario.is_valid():
        info = mi_formulario.cleaned_data
        equipos_filtrados = Equipo.objects.filter(nombre__icontains=info['nombre'])
        context ={
            "equipos": equipos_filtrados
        }

    return render(request, "AppFutbol/Busqueda_equipo.html", context=context)