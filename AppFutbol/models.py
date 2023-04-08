from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=2)
    imagen = models.ImageField(upload_to="equipos", null=True, blank=True)

    def __str__(self):
        return f"Equipo: {self.nombre}, Categoría {self.categoria}, Imagen {self.imagen}"


"""class Foto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="equipos", null=True, blank=True)
    equipo = Equipo.nombre"""


class Jugadores(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(100)

    def __str__(self):
        return f"Jugador: {self.nombre}, Apellido {self.apellido}, Edad: {self.edad}"


class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Profesor: {self.nombre}, Apellido {self.apellido}"


class Imagen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="equipos", null=True, blank=True)