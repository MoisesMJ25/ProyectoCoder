from django.urls import path
from AppFutbol.views import *

urlpatterns = [
    path('equipo/<nombre>/<categoria>', guardar_equipo),
    path('equipos', equipos),
    path('jugadores', jugadores),
    path('profesores', profesores),
]