# TerceraEntregaProyectoJP
Archivo tercera entrega ProyectoJP Django 

### Pasos para crear una pagina web con python y django

* Instalamos en nuestro ordenador el django con el comando en el terminal o cmd:

        λ pip install django

* Creamos una carpeta, en el escritorio, en mi caso llamada ProyectoJP
* Iniciar Visual Studio Code (VSC)o tu editor y pararte en esa carpeta.

* Creamos un proyecto en django, en la terminal VSC utilizamos la siguiete instrucción: 

        λ django-admin startproject ProyectoJP 

    Se crearán una serie archivos en la carpeta ProyectoJP:

    - asgi.py
    - settings.py
    - urls.py
    - views.py
    - wsgi.py
    - manage.py
    - (db.sqlite3)

    Una vez creado el Proyecto, ahora crearemos una aplicación la que llamaremos AppJP tipiando en la terminal del VSC la siguiente instrucción: 

        λ python manage.py startapp AppJP
    
    Se crearán una serie archivos en la carpeta AppJP que útiles para django:

    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py
    - (migrations)
    
    Agregaremos un archivo que no crea python y que lo utilizaremos más adelante llamado:
    - urls.py

    También deberemos agregar en nuestra aplicacion dos carpetas: la carpeta templates y la carpeta static, las que a su vez tendran otras carpetas en sun interior, tendrá esta forma:

    - (templates)
        - (AppJP) dentro de esta se crearan todos los archivos del tipo html los que coincidirán con las vista mas otro archivo llamado padre.html, el que servirá como base para poder heredar de éste las demás páginas, el listado de archivos html quedará de la siguiente manera.

                padre.html
                clientes.html
                inicio.html
                productos.html
                proveedor .html
                turnos.html
    
    Una vez creadas las plantillas html estarán vacias, mas adelante vermos como darles formato de pagina web.

    - (static)
        - (AppJP) 
            - (assents): estas conendrá archivos de de tipo imágenes.
            - (css): formato html de letras, colores, fondos, etc. 
            - (js): código javascript para movimiento o transiciones.

    De esta forma queda armado el árbol de archivos y carpetas tanto del proyecto como de la aplicación:
    
    ### Registro de la aplicación:
    Se debe registrar la aplicación, en el archivo settings perteneciente al proyecto, existen las aplicaciones de django por defecto agregaremos nuestra aplicacion, denominada AppJP.
    
    ### Application definition
        
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'AppJP',]

    ### A partir de ahora se enunciará el código contenido en los archivos comenzando por la aplicación:
    
    Archivo: **models.py**

    Este archivo generará mediante código django los campos de cada una de las bases de datos. En este caso usaremos la bbdd sqlite3

    Ej. creación de la base de datos nombre: cliente y sus campos definidos con el formato django.
        
        from django.db import models
        
        class Clientes(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        direccion = models.CharField(max_length=40)
        correo = models.EmailField(unique=True)
        telefono = models.CharField(max_length=20)
    
    de esta misma manera se crean el resto de las tablas de bases de datos que sean necesarias.

    ### Chekeo de base de datos:

    Una vez creadas todas las tablas de bbdd, lo primero que debemos hacer es checkear que las bbdd no tengan errores, en la terminal usamos el siguiente comando: 

        λ python manage.py check AppJP

    Si todo esta bien nos devolverá la terminal el siguiente mensaje:

        λ System check identified no issues (0 silenced).

    Una vez verificado las tablas de las bbdd, podemos migrar las tablas a sqlite3, usando el siguiente comando:

        λ Python manage.py makemigrations 

    Si todo sale bien nos creara las tablas:

        Migrations for 'AppJP':
        AppJP\migrations\0001_initial.py
        Create model Clientes
        Create model Productos
        Create model Proveedores
        Create model Turnos
    
    Si quisiéramos ver el código de bbdd en formato sqlite3, usamos el siguiente comando:

        λ python manage.py sqlmigrate AppJP 0001

    Por terminal aparecera la creacion de las bases de datos en lenguaje sqlite3

        BEGIN;
        -- Create model Clientes
        CREATE TABLE "AppJP_clientes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(40) NOT NULL, "apellido" varchar(40) NOT NULL, "direccion" varchar(40) NOT NULL);
        -- Create model Productos
        CREATE TABLE "AppJP_productos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(40) NOT NULL, "marca" varchar(40) NOT NULL, "proveedor" varchar(40) NOT NULL, "precio" decimal NOT NULL);
        -- Create model Proveedores
        CREATE TABLE "AppJP_proveedores" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(40) NOT NULL, "direccion" varchar(40) NOT NULL, "ciudad" varchar(40) NOT NULL, "rubro" varchar(40) NOT NULL);
        COMMIT;

    Ahora migraremos nuestas bases de datos antes creadas, con estas se crearan otras bbdd que vienen por defecto en django, para esto uilizaremos en la terminal la siguiente instruccion:

        λ python manage.py migrate

    El resultado de esta migracion será: 

        Operations to perform:
        Apply all migrations: AppCoder, admin, auth, contenttypes, sessions
        Running migrations:
        Applying AppCoder.0001_initial... OK
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK    

    En la aplicacion creara el archivo db.sqlite3

    ### Uso de tablas de bases de datos: 
    
    archivo: **views.py**
    
    La plantilla padre no figura en las vistas por que solo se usa como modelo de las demas.

    Sobre el archivo views.py, crearemos una vista de cada una de las plantillas que deban mostrar algo, creadas en tempate/AppJP, quedandonos de la siguete forma:

        from django.shortcuts import render
        from django.http import HttpResponse
        
        def inicio(request):
            return render(request, "AppJp/inicio.html")

        def cliente(request):
            return render(request, "AppJp/cliente.html")

        def proveedor(request):
            return render(request, "AppJp/proveedor.html")

        def productos(request):
            return render(request, "AppJp/productos.html")

        def turnos(request):
            return render(request, "AppJp/trunos.html")
    
    Cada vista debe tener una urls asociada a ella. Dado que el unico urls.py creado por django es el que figura en el Proyecto, para poder usar el urls.py que creamos nosotro en la aplicacion debemos indicarle al urls del proyecto que pase los url de cada vista a nuestro urls de la aplicacion, para esto usamos:

    Archivo: **urls.py del proyecto** (ProyectoJP) lo siguiente:

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
        path('admin/', admin.site.urls),
        path('AppJP/', include("AppJP.urls")),
        ]
    Donde le indicamos que incluya las urls de la aplicacion (include("AppJP.urls"))

    Archivo: **urls.py de la aplicacion** (AppJP)  lo siguiente:

        from django.urls import path
        from AppJP.views import *

        urlpatterns = [
        path("inicio/", inicio, name="Inicio"),
        path('cliente/', cliente, name="Clientes"),
        path('proveedor/', proveedor, name="Proveedores"),
        path('producto/', productos, name = "Productos"),
        path('turno/', turnos, name= "Turnos"),
        ]

    
    ### Plantillas html:

    archivo: **padre.html**

    Para esta plantilla usaremos una pagina web completa de Bootstrap buscando en un sitio que tiene plantillas gratis, se denomina startbootstrap.com. Elegiremo una y bajaremos todo su contenido:

        init.html : El cual contiene el codigo de html
        (asset) : carpeta con todas las fotos de la pagina
        (css) : capeta con todo el formato css de la pagina
        (js) : carpeta con los archivos script de javascrip
    
    * El archivo init,html lo cipiaremos y pegaremos en la plantilla denominada padre.html. 
    * En la plantilla padre.html debermos cambiar los vinculos de bootstrap por vinculos de django, es decir lso vinculos:
    Dentro del head debemos escribir:
        
        {% load static %} : instruccion que indica que deben cargarse todos los archivos entro la carpeta (static). Estos son las imagenes, js y css.
        
        La ruta de referencia **href** y **src** de bootstrap como: sera reemplazado por:
        
        <href="assets/favicon.ico" /> 
        
        src="{js/scripts.js}"

        Las  ruta de referencias de bootstrap seran reemplazadas respectivamente por:
       
        <href="{% static 'AppJP/assets/favicon.ico' %}" /> 
        
        src="{% static 'AppJP/js/scripts.js' %}" 
        
        En el caso de que las referencias sean a sitios web no es necesario reemplazarlos.

    ### Adaptacion de nuestra plantilla padre.html generica de bootstrap:

    - Se cambiarán los texto de botones a nuestro tema:

        Para que el boton abra una nueva plantilla hija, debemos cambiar el url del boton y para esto usaremos como url el **name="Inicio"** que se uso en el archivo urls.py de la aplicacion, por ejemplo el nombre de inicio. 
        
           path("inicio/", inicio, **name="Inicio"**),
        
        en la pagina padre si quermos que el boton inicio vaya a  **Inicio** esto se aplicaria así:

            <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded" href="{% url 'inicio'%}">Inicio</a></li>

    - Se eliminarán parate del codigo que no se necesite.
    - Tambien se reemplazaan las imagenes.
    
    ### Reutilizacion con herencia de la plantilla padre.html en el resto de las plantillas.

    Para que una plantilla hijo como inicio.html de una plantilla padre.html en el hijo deberemos escribir en la primera lineas, el uso de extender la plantilla padre a la hija y la lectura de la carpeta static:

        {% extends "AppJP/padre.html" %}
        {% load static %}
    
    Si heredamos la plantilla padre.htm para todas las demas platillas, esto se hace para el formato, no para los titulos y o textos particulares de cada plantilla. Para estos casos usamos el bloque de django. 
        
    - En la plantilla padre se reemplaza el texto (por ej. el titulo) por un bloque con nombre vacio: 

        {% block titulo %}
                                    sin texto    
        {% endblock %}

    - En la plantilla hijo se reemplaza el texto (por ej. el titulo) por un bloque con nombre vacio: 

        {% block titulo %}
            BIENVENIDOS AL INICIO
        {% endblock %}

