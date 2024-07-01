from django.shortcuts import render
from negocio.models import *

from negocio.forms import *

# Create your views here.

def home(request):
    return render(request, "negocio/index.html")

def proveedores(request):
    contexto = {"proveedores": Proveedor.objects.all()}
    return render(request, "negocio/proveedores.html", contexto)

def usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request, "negocio/usuarios.html", contexto)


def libros(request):
    libros = Libro.objects.all()
    contexto = {"libros": libros}
    return render(request, "negocio/libros.html", contexto)


## ________________Formularios

def usuariosForm(request):
    
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            nombre_usuario = miForm.cleaned_data.get("nombre")
            direccion_usuario = miForm.cleaned_data.get("direccion")
            email_usuario = miForm.cleaned_data.get("email")
            telefono_usuario = miForm.cleaned_data.get("telefono")
            usuario = Usuario(nombre=nombre_usuario, direccion=direccion_usuario, email=email_usuario, telefono=telefono_usuario)
            usuario.save()
            contexto = {"usuarios": Usuario.objects.all() }
            return render(request, "negocio/usuarios.html", contexto)
    else:
        miForm = UsuarioForm()
    
    return render(request, "negocio/usuarioForm.html", {"form": miForm})

def librosForm(request):
    
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            titulo_libro = miForm.cleaned_data.get("titulo")
            autor_libro = miForm.cleaned_data.get("autor")
            anio_libro = miForm.cleaned_data.get("anio")
            genero_libro = miForm.cleaned_data.get("genero")
            libro = Libro(titulo=titulo_libro, autor=autor_libro, anio=anio_libro, genero=genero_libro)
            libro.save()
            contexto = {"libros": Libro.objects.all() }
            return render(request, "negocio/libros.html", contexto)
    else:
        miForm = LibroForm()
    
    return render(request, "negocio/librosForm.html", {"form": miForm})


def proveedoresForm(request):
    
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            nombre_proveedor = miForm.cleaned_data.get("nombre")
            email_proveedor = miForm.cleaned_data.get("email")
            telefono_proveedor = miForm.cleaned_data.get("telefono")
            proveedor = Proveedor(nombre=nombre_proveedor, email=email_proveedor, telefono=telefono_proveedor)
            proveedor.save()
            contexto = {"proveedores": Proveedor.objects.all() }
            return render(request, "negocio/proveedores.html", contexto)
    else:
        miForm = ProveedorForm()
    
    return render(request, "negocio/proveedorForm.html", {"form": miForm})

## Buscar

def buscarLibros(request):
    return render(request, "negocio/buscarLibros.html")

def encontrarlibros(request):
    if request.GET["buscar"]:
        libro = request.GET["buscar"]
        titulos = Libro.objects.filter(titulo__icontains=libro)
        contexto = {'libros': titulos}
    else:
        contexto = {'libros': Libro.objects.all()}
        
    return render(request, "negocio/libros.html", contexto)