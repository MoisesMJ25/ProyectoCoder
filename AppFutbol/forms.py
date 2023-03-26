from django import forms


class EquipoForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    categoria = forms.CharField(min_length=2)


class JugadorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    apellido = forms.CharField(min_length=4, max_length=10)
    edad = forms.IntegerField(max_value=2)


class ProfesorForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    apellido = forms.CharField(min_length=4, max_length=10)
    email = forms.EmailField(min_length=10)