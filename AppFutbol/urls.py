from django.urls import path
from AppFutbol.views import *

urlpatterns = [
    path('equipos', equipos, name="AppFutbolEquipos"),
    path('equipo/crear', crear_equipo, name="AppFutbolCrearEquipo"),
    path('jugador/crear', crear_jugador, name="AppFutbolCrearJugador"),
    path('profesor/crear', crear_profesor, name="AppFutbolCrearProfesor"),
    path('jugadores', jugadores, name="AppFutbolJugadores"),
    path('profesores', profesores, name="AppFutbolProfesores"),
    path('home', home, name='inicio'),
    path('busqueda_equipo', busqueda_equipo, name='AppFutbolBusquedaEquipo'),
    path('busqueda_jugador', buscar_jugador, name='AppFutbolBusquedaJugador'),
    path('busqueda_profesor', buscar_profesor, name='AppFutbolBusquedaProfesor'),
    path('equipos/eliminar/<id>', eliminar_equipo, name='AppFutbolEliminarEquipo'),
    path('equipos/editar/<id>', editar_equipo, name='AppFutbolEditarEquipo'),
    path('jugadores/eliminar/<id>', eliminar_jugador, name='AppFutbolEliminarJugador'),
    path('jugadores/editar/<id>', editar_jugador, name='AppFutbolEditarJugador'),
    path('profesores/eliminar/<id>', eliminar_profesor, name='AppFutbolEliminarProfesor'),
    path('profesores/editar/<id>', editar_profesor, name='AppFutbolEditarProfesor'),
]