from django import forms


class EntradaForm(forms.Form):
    nombre= forms.CharField(max_length=255)
    descripcion= forms.CharField(max_length=255)
    precio= forms.IntegerField()

class PrincipalForm(forms.Form):
    nombre= forms.CharField(max_length=255)
    descripcion= forms.CharField(max_length=255)
    precio= forms.IntegerField()

class PostreForm(forms.Form):
    nombre= forms.CharField(max_length=255)
    descripcion= forms.CharField(max_length=255)
    precio= forms.IntegerField()