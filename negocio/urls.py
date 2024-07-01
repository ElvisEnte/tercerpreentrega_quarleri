from django.urls import path
from negocio.views import *


urlpatterns = [
    path('', home, name="home"),
    path('proveedores/', proveedores, name="proveedores"),
    path('usuarios/', usuarios, name="usuarios"),
    path('libros/', libros, name="libros"),
    
    ## Formularios
    path('usuarioForm/', usuariosForm, name="usuarioForm"),
    path('proveedorForm/', proveedoresForm, name="proveedoresForm"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('encontrarlibros/', encontrarlibros, name="encontrarlibros")
    
]
