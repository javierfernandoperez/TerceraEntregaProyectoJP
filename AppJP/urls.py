from django.urls import path
from AppJP.views import *


urlpatterns = [
    path("inicio/", inicio, name="Inicio"),
    path('cliente/', cliente, name="Clientes"),
    path('proveedor/', proveedor, name="Proveedores"),
    path('producto/', productos, name = "Productos"),
    path('turno/', turnos, name= "Turnos"),
    path('formsClientes/', formsClientes, name="clientesForms"),
    path('formsProveedores/', formsProveedores, name="proveedoresForms"),
    path('formsProductos/', formsProductos, name="productosForms"),
    path('formsTurnos/', formsTurnos, name="turnosForms"),
    path('buscaCliente/', buscaCliente, name="clienteBusca"),
    path('resultadoCliente/', resultadoCliente, name="clienteResulado"),
    path('buscaProducto/', buscaProducto, name="productoBusca"),
    path('resultadoProducto/', resultadoProducto, name="productoResulado"),
    path('buscaProveedor/', buscaProveedor, name="proveedorBusca"),
    path('resultadoProveedor/', resultadoProveedor, name="proveedorResulado"),
    path('buscaTurno/', buscaTurno, name="turnoBusca"),
    path('resultadoTurno/', resultadoTurno, name="turnoResulado"),
]