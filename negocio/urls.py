from django.urls import path
from negocio.views import *


urlpatterns = [
    path('', home, name="home"),
    path('proveedores/', proveedores, name="proveedores"),
    path('usuarios/', usuarios, name="usuarios"),
    path('libros/', libros, name="libros"),
]
