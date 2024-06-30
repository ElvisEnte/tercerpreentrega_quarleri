from django.db import models

import random

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto_email = models.EmailField()
    contacto_telefono = models.IntegerField()
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.IntegerField()
    
class Libros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=100)