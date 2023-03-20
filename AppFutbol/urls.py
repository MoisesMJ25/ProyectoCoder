from django.urls import path
from AppFutbol.views import guardar_equipo, equipos, jugadores, profesores

urlpatterns = [
    path('equipo/<nombre>', guardar_equipo),
    path('equipos', equipos),
    path('jugadores', jugadores),
    path('profesores', profesores),
]