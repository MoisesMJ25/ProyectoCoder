from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from AppFutbol.models import Equipo, Jugadores, Profesores
from AppFutbol.forms import (EquipoForm,
                             JugadorForm,
                             ProfesorForm,
                             BusquedaEquipoForm,
                             BusquedaJugadorForm,
                             BusquedaProfesorForm)


def home(request):
    return render(request, "base.html")


# VISTAS EQUIPO

def equipos(request):

    all_equipos = Equipo.objects.all()
    context = {
        "equipos": all_equipos,
        "form_busqueda": BusquedaEquipoForm(),
    }
    return render(request, "AppFutbol/equipos.html", context=context)

#@login_required
def crear_equipo(request):
    if request.method == "POST":
        mi_formulario = EquipoForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            equipo_save = Equipo(
                nombre=info['nombre'],
                categoria=info['categoria']
            )
            equipo_save.save()
            return redirect("AppFutbolEquipos")
    context = {
        "form": EquipoForm()
    }
    return render(request, "AppFutbol/crear_equipo.html", context=context)


def editar_equipo(request, id):
    get_equipo = Equipo.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = EquipoForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data

            get_equipo.nombre = info['nombre']
            get_equipo.categoria = info['categoria']

            get_equipo.save()
            return redirect("AppFutbolEquipos")

    context = {
        "id": id,
        "form": EquipoForm(initial={
            "nombre": get_equipo.nombre,
            "categoria": get_equipo.categoria,
        })
    }
    return render(request, "AppFutbol/editar_equipo.html", context=context)

def busqueda_equipo(request):
    # mostrar datos filtrados
    mi_formulario = BusquedaEquipoForm(request.GET)
    if mi_formulario.is_valid():
        info = mi_formulario.cleaned_data
        equipos_filtrados = Equipo.objects.filter(nombre__icontains=info['nombre'])
        context = {
            "equipos": equipos_filtrados
        }

    return render(request, "AppFutbol/Busqueda_equipo.html", context=context)

@login_required
def eliminar_equipo(request, id):
    get_equipo = Equipo.objects.get(id=id)
    get_equipo.delete()

    return redirect("AppFutbolEquipos")





# VISTAS JUGADOR

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

def crear_jugador(request):
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
            return redirect("AppFutbolJugadores")
    context = {
        "form": JugadorForm()
    }
    return render(request, "AppFutbol/crear_jugador.html", context=context)

def editar_jugador(request, id):
    get_jugador = Jugadores.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = JugadorForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data

            get_jugador.nombre = info['nombre']
            get_jugador.apellido = info['apellido']
            get_jugador.edad = info['edad']

            get_jugador.save()
            return redirect("AppFutbolJugadores")

    context = {
        "id": id,
        "form": JugadorForm(initial={
            "nombre": get_jugador.nombre,
            "apellido": get_jugador.apellido,
            "edad": get_jugador.edad,
        })
    }
    return render(request, "AppFutbol/editar_jugador.html", context=context)

def buscar_jugador(request):
    # mostrar datos filtrados
    mi_formulario = BusquedaJugadorForm(request.GET)
    if mi_formulario.is_valid():
        info = mi_formulario.cleaned_data
        jugadores_filtrados = Jugadores.objects.filter(nombre__icontains=info['nombre'])
        context = {
            "jugadores": jugadores_filtrados
        }

    return render(request, "AppFutbol/Busqueda_jugador.html", context=context)

def eliminar_jugador(request, id):
    get_jugador = Jugadores.objects.get(id=id)
    get_jugador.delete()

    return redirect("AppFutbolJugadores")





# VISTAS PROFESOR

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

def crear_profesor(request):
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
            return redirect("AppFutbolProfesores")
    context = {
        "form": ProfesorForm()
    }
    return render(request, "AppFutbol/crear_profesor.html", context=context)

def editar_profesor(request, id):
    get_profesor = Profesores.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data

            get_profesor.nombre = info['nombre']
            get_profesor.apellido = info['apellido']
            get_profesor.email = info['email']

            get_profesor.save()
            return redirect("AppFutbolProfesores")

    context = {
        "id": id,
        "form": ProfesorForm(initial={
            "nombre": get_profesor.nombre,
            "apellido": get_profesor.apellido,
            "email": get_profesor.email
        })
    }
    return render(request, "AppFutbol/editar_profesor.html", context=context)

def buscar_profesor(request):
    # mostrar datos filtrados
    mi_formulario = BusquedaProfesorForm(request.GET)
    if mi_formulario.is_valid():
        info = mi_formulario.cleaned_data
        profesores_filtrados = Profesores.objects.filter(nombre__icontains=info['nombre'])
        context = {
            "profesores": profesores_filtrados
        }

    return render(request, "AppFutbol/Busqueda_profesor.html", context=context)

def eliminar_profesor(request, id):
    get_profesor = Profesores.objects.get(id=id)
    get_profesor.delete()

    return redirect("AppFutbolProfesores")