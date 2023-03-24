from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return f"Equipo: {self.nombre}, Categoría {self.categoria}"

class Jugadores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(2)

    def __str__(self):
        return f"Jugador: {self.nombre}, Apellido {self.apellido}, Edad: {self.edad}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Profesor: {self.nombre}, Apellido {self.apellido}"