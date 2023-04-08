from django.contrib import admin
from AppFutbol.models import Equipo, Jugadores, Profesores, Imagen

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Jugadores)
admin.site.register(Profesores)
admin.site.register(Imagen)