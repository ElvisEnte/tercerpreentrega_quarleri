from django.shortcuts import render
from negocio.models import *

# Create your views here.

def home(request):
    return render(request, "negocio/index.html")

def proveedores(request):
    contexto = {"proveedores": Proveedor.objects.all()}
    return render(request, "negocio/proveedores.html", contexto)

def usuarios(request):
    return render(request, "negocio/usuarios.html")


def libros(request):
    return render(request, "negocio/libros.html")