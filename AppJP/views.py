from django.shortcuts import render
from django.http import HttpResponse
from AppJP.models import Clientes, Proveedores, Productos, Turnos
from AppJP.forms import FormsClientes, FormsProveedores, FormsProductos, FormsTurnos

def inicio(request):
    return render(request, "AppJp/inicio.html")

def cliente(request):
    return render(request, "AppJp/cliente.html")

def proveedor(request):
    return render(request, "AppJp/proveedor.html")

def productos(request):
    return render(request, "AppJp/productos.html")

def turnos(request):
    return render(request, "AppJp/turnos.html")
    
def formsClientes(request):
    if request.method == "POST":
        formulario = FormsClientes(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            clientes = Clientes(nombre = info["nombre"],apellido = info["apellido"], direccion = info["direccion"], correo=info["correo"], telefono=info["telefono"] )
            clientes.save()
            return render(request, "AppJP/inicio.html")
    else:
        formulario = FormsClientes()
        return render(request, "AppJP/formsClientes.html", {"forCli": formulario})

def formsProveedores(request):
    if request.method == "POST":
        formulario = FormsProveedores(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            proveedor = Proveedores(nombre_prov = info["nombre_prov"],direccion_prov = info["direccion_prov"], ciudad = info["ciudad"], rubro=info["rubro"])
            proveedor.save()
            return render(request, "AppJP/inicio.html")
    else:
        formulario = FormsProveedores()
        return render(request, "AppJP/formsProveedores.html", {"forPrv": formulario})

def formsProductos(request):
    if request.method == "POST":
        formulario = FormsProductos(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Productos(nombre_prod=info["nombre_prod"], tratami_prod=info["tratami_prod"], marca=info["marca"], precio=info["precio"])
            producto.save()
            return render(request, "AppJP/inicio.html")
    else:
        formulario = FormsProductos()
        return render(request, "AppJP/formsProductos.html", {"forPro": formulario})
    
def formsTurnos(request):
    if request.method == "POST":
        formulario = FormsTurnos(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            turno = Turnos(fecha = info["fecha"],hora = info["hora"], tratamiento = info["tratatmiento"])
            turno.save()
            return render(request, "AppJP/inicio.html")
    else:
        formulario = FormsTurnos()
        return render(request, "AppJP/formsTurnos.html", {"forTur": formulario})
    
def buscaCliente(request):
    return render(request, "AppJP/buscaCliente.html")

def resultadoCliente(request):
    
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Clientes.objects.filter(nombre__icontains = nombre)
        return render(request, "AppJP/resultadoCliente.html", {"clientes": clientes, "nombre": nombre})
        
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def buscaProveedor(request):
    return render(request, "AppJP/buscaProveedor.html")


def resultadoProveedor(request):
    
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        proveedores= Proveedores.objects.filter(nombre_prov__icontains = nombre)
        return render(request, "AppJP/resultadoProveedor.html", {"proveedores": proveedores, "nombre": nombre})
        
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def buscaProducto(request):
    return render(request, "AppJP/buscaProducto.html")

def resultadoProducto(request):
    
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Productos.objects.filter(nombre_prod__icontains=nombre)
        return render(request, "AppJP/resultadoProducto.html", {"productos": productos, "nombre": nombre})
        
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    

def buscaTurno(request):
    return render(request, "AppJP/buscaProveedor.html")


def resultadoTurno(request):

    if request.GET["nombre"]:
        dia = request.GET["dia"]
        turnos = Turnos.objects.filter(nombre__icontains=dia)
        return render(request, "AppJP/resultadoTurnos.html", {"turnos": turnos, "dia": dia})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
