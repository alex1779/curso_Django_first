from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido


def saludo(request):    #primera vista

    #nombre="Alejandro"

    #apellido="Maggioni"

    per1 = Persona("Alitos", "maggioni1")

    momentoActual = datetime.datetime.now()

    doc_externo=open("/home/rafa/Escritorio/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":per1.nombre, "apellido_persona":per1.apellido, "momento_actual":momentoActual, "temas":["Modelos", "Formularios", "Vistas", "Despliegue"]})

    documento=plt.render(ctx)

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
