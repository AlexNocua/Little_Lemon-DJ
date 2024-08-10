from django.db import models
from django.contrib import admin
# importacion de la api de forms
from django import forms
# Create your models here.

# creacion de un modelo de reservacion


class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField("Phone number", max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    list_display = ('Name',)
    # def __str__(self):
    #     return f'Nombre:{self.name}'

# clase para mostrar los datos en tipo de columna


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'time', 'count', 'notes')


# #creacion de un modelo de ejemplo de un menu
class Menu(models.Model):
    nombreproducto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000, default='')
    cantidad_producto = models.IntegerField()
    # ajustes de binarizacion para el almacenaje de archivos como imagenes
    imagen = models.BinaryField(null=True, blank=True)

# class MenuAdmin(admin.ModelAdmin):
class MenuForm(forms.ModelForm):
    # Se tiene que crear un campo adicional para subir la imagen
    imagen_file = forms.ImageField(required=False)

    class Meta:
        model = Menu
        exclude =['imagen']
        list_display = ('nombreproducto', 'cantidad_producto', 'imagen_file', 'descripcion')

    def save(self, commit=True):
        instancia = super().save(commit=False)
        if self.cleaned_data['imagen_file']:
            imagen_ = self.cleaned_data['imagen_file']
            instancia.imagen = imagen_.read()
        if commit:
            instancia.save()
        return instancia
            

    # metodo salvar para guardar la imagen desde el panel admin


# creacion de la clase formulario
class FormComunicate(models.Model):
    nombre = models.CharField(verbose_name='Tu nombre', max_length=100)
    correo = models.EmailField(verbose_name='Correo', max_length=100)
    opinion = models.TextField(
        verbose_name='Cuéntanos tu opinión', max_length=500)
    

#visualizacion en el admin
class FormComunicateAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'opinion')