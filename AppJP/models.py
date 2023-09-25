from django.db import models

    
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
   
class Proveedores(models.Model):
    nombre_prov = models.CharField(max_length=40)
    direccion_prov = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    rubro = models.CharField(max_length=40)

class Productos(models.Model):
    nombre_prod = models.CharField(max_length=40)
    tratami_prod = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.FloatField()
    
class Turnos(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    tratamiento = models.CharField(max_length=40)
    