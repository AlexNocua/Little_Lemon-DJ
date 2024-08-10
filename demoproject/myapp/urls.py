# newapp/urls.py
from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('principal/', views.principal, name='principal'),
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('comunicate/', views.comunicate, name='comunicate'),
    path('opiniones/', views.opiniones, name='opiniones'),
    path('menu_item/<id>', views.menu_item, name='menu_item'),
]
