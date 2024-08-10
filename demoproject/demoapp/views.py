import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import loader
from django.views import View
from .forms import DemoForm, ClaseForm
from django.urls import reverse

# class MyView(View):
#     def get(self, request):
#         # logic to process GET request
#         return HttpResponse('response to GET request')

#     def post(self, request):
#         return HttpResponse('response to POST request')
# user = {
#     'user_id': 1,
#     'name': 'Alex',
#         # <logic to process POST request>
#     'DNI': '1003'
# }

# def user_by_id(request, user_id):
#     user = {
#         'user_id': '1',
#         'name': 'Alex',
#         'DNI': '1003'
#     }
#     # muestra de retorno HTTP
#     # return HttpResponse(f'El usuario registrado con el nombre {user["name"]} \n Su DNI es: {user["user_id"]}')
#     # muestra de renderizacion del template
#     # diferencia de envio de datos con flask, este se deve enviar como un diccionario
#     return render(request, 'datos.html', {'user': user})


def ejemplo_render_httpresponse(request):
    path = request.path
    template = loader.get_template('Plantilla.html')
    context = {'mensaje': f'Hola desde Python: {path}', }
    return HttpResponse(template.render(context, request))


def index(request):
    path = request.path
    method = request.method
    content = '''
    <center>
    <h1>Testing Django Request Response Objects</h1>
    <p>Request path :{}</p>
    <p>Request method:{}</p>
  </center>
    
    '''.format(path, method)
    return HttpResponse(content)

# este es un ejemplo de manejo de mensajes segun la solicitud
# def index(request):

#     if request.method == 'GET':
#         return HttpResponse("""
#                         <style>
#                         h1{
#                             color: red;
#                         }
#                         </style>
#                         <h1>Hello, world. This is the index view of Demoapp. <br>Este es el metodo GET</h1>""")
#     elif request.method == 'POST':
#         return HttpResponse('Este es  el metodo POST')


# Informacion del encabezado de las requisiciones de oslicirudes y respuestas
def information(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    # otra manera de retornar
    # response = HttpResponse('This works')

    response = HttpResponse()
    response.headers['Age'] = 20
    # tambien se puede mostrar una cadena como un mensaje
    msg = f'''
      <br>Path:{path}
  <br>Address:{address}
  <br>Scheme:{scheme}
  <br>Method:{method}
  <br>User agent:{user_agent}
  <br>Path info:{path_info}
  <br>
     <br>Response headers:{response.headers}
 
    
    
    
    '''
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


# definicion de funciones para dar parametros en urls

def pathview(request, name, id):
    tipo_dato1 = type(name).__name__
    tipo_dato2 = type(id).__name__

    return HttpResponse('Name: {} UserID: {} \n Estos son los tipos de datos recibidos: 1.|{}| 2.|{}|  '.format(name, id, tipo_dato1, tipo_dato2))

# definicion de la vista de la URL con los parametros de consulta


def qryview(request):
    nombre = request.GET['nombre']
    id_ = request.GET['id']

    return HttpResponse('''
                      El nombre cosultado fue: {}
                      El id de la persona consutada es: {}
                      '''.format(nombre, id_))
    # ejemplo de URL de consulta http://127.0.0.1:8000/getuser/?nombre=Alex&id=14


# renderizacion de el formulario para el envio de datos

def showform(request):
    return render(request, 'form.html')

# respuesta de la plantilla donde se van a mostrar los datos ingresados en el formulario


def getform(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']

    return HttpResponse('Nombre ingresado: {} ID ingresado: {}'.format(name, ID))


# creacion de la vista del fomulario de ejmplo en el archivo forms
def ejemploform(request):
    form = DemoForm()
    return render(request, 'form_form.html', {'form': form})


# creacion de la vista del formulario modelo
def exampleformmodel(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            # datos = ClaseForm(request.POST)recuperacion de los datos
            # nombre = request.POST['Primer_Nombre']
        # return HttpResponse(f' {nombre}')
            return redirect('demoapp:exampleformmodel')
        else:
            errors = form.errors.as_json()
            return HttpResponse(f'Errores de validación: {errors}')

    else:
        form = ClaseForm()
    context = {'form': form}
    return render(request, 'claseForm.html', context)
