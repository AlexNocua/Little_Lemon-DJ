from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Menu, FormComunicate

# importacion para la base64
import base64

# importacion de la clase Formulario
from .forms import FormComunicateForm
# Create your views here.


def home(request):
    return HttpResponse('Bienvenido a Little Lemon')


def about(request):
    return HttpResponse('Acerca de nosotros')


def menu(request):
    return HttpResponse('Menú de Little Lemon')


def reservation(request):
    return HttpResponse('Hacer una reserva')

# vista de la vista principal de Little Lemon


def principal(request):
    return render(request, 'base.html')

# vista de renderizacion del contenido osobre nosotros


def inicio(request):
    return render(request, 'inicio.html')


def sobre(request):
    return render(request, 'sobre.html')

# renderizaacion de la vista de opinones


def opiniones(request):
    content = FormComunicate.objects.all()
    context = {'content': content}
    return render(request, 'opiniones.html', context)
# vista para la visualizacion y dinamismo de datos de un modelo


#!esta va a ser una funcion con la cual se va a retornar pasar de objeto a diccionario
#! con la imagen tambien para mostrarla

# ? Tener en cuenta que este solo se utiliza cuando se reciven mas objetos, en dado caso dada uno de estos objetos
# ? se guarda en una lista y se extraen por medio de un for en las plantillas
def retornar_diccionario(objeto):
    # Convertir imágenes a base64 y añadir al contexto
    list_menus = []
    for item in objeto:
        imagen_base64 = base64.b64encode(item.imagen).decode(
            'utf-8') if item.imagen else ''
        imagen_url = f"data:image/jpeg;base64,{imagen_base64}" if imagen_base64 else ''

        list_menus.append({
            'nombreproducto': item.nombreproducto,
            'cantidad_producto': item.cantidad_producto,
            'descripcion': item.descripcion,
            'imagen_url': imagen_url,
            'id': item.id,
        })
    objeto = {'content': list_menus}
    return objeto


def menu(request):
    # Trae todos los objetos del modelo Menu
    content = Menu.objects.all()
    context = retornar_diccionario(content)
    return render(request, 'menu.html', context)


# creacion de la vista del modelo formulario

def comunicate(request):
    if request.method == 'POST':
        form = FormComunicateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:comunicate')
        else:
            return HttpResponse('Ocurrio Algo')
    else:
        form = FormComunicateForm()
        context = {'form': form}
        return render(request, 'comunicate.html', context)


# creacion de la vista de informacion del menu
def menu_item(request, id=None):
    if id:
        menu_item = Menu.objects.get(id=id)

        # ? en este caso como solo es un objeto se accede directamente a el y se crea uno nuevo sustituyendo el valor de la imagen
        imagen_base64 = base64.b64encode(menu_item.imagen).decode(
            'utf-8') if menu_item.imagen else ''
        imagen_url = f"data:image/jpeg;base64,{imagen_base64}" if imagen_base64 else ''

        menu = {
            'nombreproducto': menu_item.nombreproducto,
            'cantidad_producto': menu_item.cantidad_producto,
            'descripcion': menu_item.descripcion,
            'imagen_url': imagen_url,
            'id': menu_item.id,
        }

        context = {'menu_info': menu}
        return render(request, 'menu_item.html', context)

    return HttpResponse(f'{id}')
