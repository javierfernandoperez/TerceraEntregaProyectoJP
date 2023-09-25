from django import forms


class FormsClientes(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    direccion = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.CharField()

class FormsProveedores(forms.Form):
    nombre_prov = forms.CharField()
    direccion_prov = forms.CharField()
    ciudad = forms.CharField()
    rubro = forms.CharField()

class FormsProductos(forms.Form):
    nombre_prod = forms.CharField()
    tratami_prod = forms.CharField()
    marca = forms.CharField()
    precio = forms.FloatField()

class FormsTurnos(forms.Form):
    fecha = forms.DateField()
    hora = forms.TimeField()
    tratamiento = forms.CharField()
