from django.urls import path

from . import views
app_name = 'demoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('Renderizada_Http_response', views.ejemplo_render_httpresponse,
         name='ejemplo_render_httpresponse'),
    path('information_request_response', views.information, name='information'),

    # path('Usuario/<int:user_id>', views.user_by_id, name= 'user_by_id'),
    # otra forma de parametro en url
    path('usuario/<name>/<id>', views.pathview, name='pathview'),

    # definicion de vista con parametros de consulta
    path('getuser/', views.qryview, name='qryview'),

    # definicion de la vista del formulario
    path('showform/', views.showform, name='showform'),

    # definicion de la URL para mostrar los datos ingresados en el form
    path('getform/', views.getform, name='getform'),

    # definicion de la ruta para las clases formilario
    path('ejemploform/', views.ejemploform),

    # creacion de la ruta de ejemplo de clase formulario para la creacio ndel mismo y el envio de los datos a la base de datos
    # es importante al momento de redireccinar a la misma vista, incluir el nombre de la vista oara utilizarlo con el urlpaterns
    path('exampleformmodel/', views.exampleformmodel, name = 'exampleformmodel'),
]
