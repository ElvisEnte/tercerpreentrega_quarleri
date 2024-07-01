from django.db import models


# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto_email = models.EmailField()
    contacto_telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        ordering = ["titulo", "autor"]