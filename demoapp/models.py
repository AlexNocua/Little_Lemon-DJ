from django.db import models

# Create your models here.


class Menu(models.Model):

    name = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=50)
    price = models.IntegerField()
  
    def __str__(self):
        return self.name + ' : ' + self.cuisine


class Menuitems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()

    # recordar que cunaod se ejecute la clase me muestre la funcion:

    def __str__(self):
        return self.name + ':' + self.couese



# creacion del modelo formulario
class Logger(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Fecha = models.CharField(max_length=100)
