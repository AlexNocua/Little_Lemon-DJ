from django import forms
from django.forms.widgets import NumberInput
from .models import FormComunicate

# creacion de la clase Form


class FormComunicateForm(forms.ModelForm):
    class Meta:
        model = FormComunicate
        fields = ['nombre', 'correo', 'opinion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Tu nombre',
                'style': 'width: 300px; border: 1px solid #ccc; margin: 10px;padding: 10px;',
                'class': 'custom-class'
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'Correo',
                'style': 'width: 300px; border: 1px solid #ccc; margin: 10px;padding: 10px;',
                'class': 'custom-class'
            }),
            'opinion': forms.Textarea(attrs={
                'placeholder': 'Cuéntanos tu opinión',
                'style': 'width: 300px; height: 100px; border: 1px solid #ccc; margin: 10px;padding: 10px;display:flex;flex-direction:colum;',
                'class': 'custom-class'
            }),
        }
