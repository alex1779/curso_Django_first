from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):

    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido


def saludo(request):    #primera vista

    #nombre="Alejandro"

    #apellido="Maggioni"

    temasDelCurso=["Modelos", "Formularios", "Vistas", "Despliegue"]

    per1 = Persona("ale", "maggioni")

    momentoActual = datetime.datetime.now()

    #doc_externo=open("/home/rafa/Escritorio/ProyectosDjango/curso_Django_first/Proyecto1/plantillas/miplantilla.html")

    #plt=Template(doc_externo.read())

    #doc_externo.close()

    doc_externo=get_template('miplantilla.html')

    #ctx=Context({"nombre_persona":per1.nombre, "apellido_persona":per1.apellido, "momento_actual":momentoActual, "temas":temasDelCurso})

    documento=doc_externo.render({"nombre_persona":per1.nombre, "apellido_persona":per1.apellido, "momento_actual":momentoActual, "temas":temasDelCurso})

    return HttpResponse(documento)


def despedida(request):

    return HttpResponse("hasta luego amigos")


def dameFecha(request):

    fechaActual = datetime.datetime.now()

    documento = """
    <html>
        <body>
            <h1>
                Fecha y hora actual %s
            </h1>
        </body>
    </html>
    """ %fechaActual

    return HttpResponse(documento)


def calculaEdad(request, edad, agno):

    edadActual=edad
    periodo=agno-2023
    edadFutura=edadActual+periodo

    documento = """
    <html>
        <body>
            <h1>
                En el anio %s tendras %s anios
            </h1>
        </body>
    </html>
    """ %(agno, edadFutura)
    return HttpResponse(documento)
