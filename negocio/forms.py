from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=200, required=True)
    email = forms.CharField(max_length=100, required=True)
    telefono = forms.IntegerField(required=True)
    
class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=200, required=True, label="Contacto Comercial")
    telefono = forms.IntegerField(required=True)
    
class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=200, required=True)
    anio = forms.IntegerField(required=True, label="Año")
    genero = forms.CharField(max_length=100, required=True)