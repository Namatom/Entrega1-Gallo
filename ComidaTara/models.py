from django.db import models
from django.forms import IntegerField

# Create your models here.
class Entrada(models.Model):
    nombre= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=255)
    precio= models.IntegerField()

    def __str__(self):
        return self.nombre


class Principal(models.Model):
    nombre= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=255)
    precio= models.IntegerField()

    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=255)
    precio= models.IntegerField()

    def __str__(self):
        return self.nombre