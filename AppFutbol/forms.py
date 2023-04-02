from django import forms


class EquipoForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    categoria = forms.CharField(min_length=2)

class JugadorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    apellido = forms.CharField(min_length=4, max_length=10)
    edad = forms.IntegerField(max_value=100)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    apellido = forms.CharField(min_length=4, max_length=10)
    email = forms.EmailField(min_length=10)

class BusquedaEquipoForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)

class BusquedaProfesorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)