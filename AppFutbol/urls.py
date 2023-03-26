from django.urls import path
from AppFutbol.views import *

urlpatterns = [
    path('equipos', equipos, name="AppFutbolEquipos"),
    path('equipo/<nombre>/<categoria>', guardar_equipo, name="AppFutbolEquipo"),
    path('jugadores', jugadores, name="AppFutbolJugadores"),
    path('profesores', profesores, name="AppFutbolProfesores"),
    path('home', home, name='inicio'),
]