from django import forms
from django.forms.widgets import NumberInput
from .models import Logger


# creacion de un formulario simple
role_choises = [('italian', 'Itaian'), ('colombia',
                                        'Colombia'), ('brasil', 'Brasil')]


class DemoForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(max_length=100, label='Ingresa tu email')
    reservation_date = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}))
    role = forms.ChoiceField(choices=role_choises)
    role_type_radioselect = forms.ChoiceField(
        widget=forms.RadioSelect, choices=role_choises)


# uso de la clase formulario para la creacion y envio de los datos a la base ded atos directamente
class ClaseForm(forms.ModelForm):
    class Meta:
        # esta es igual a la creacion del modelo del formulario
        model = Logger
        # este es para traer todos los campos del modelo
        fields = '__all__'


# Anteproyecto ={
#     'nombre':'CIGAP',
#     'Integrante_1': 'Alex Nocua'
# }

# proyectos={
#     'proyecto1':Anteproyecto,
#     'proyecto3':proyecto,
#     'proyecto3':proyecto
# }

# proyectos['']