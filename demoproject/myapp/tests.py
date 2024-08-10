from django.test import TestCase
# importacion de los modelos
from .models import FormComunicate
# Create your tests here.



class FormComunicateModelTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.formcomunicate= FormComunicate.objects.create(
            nombre = 'Alex',
            correo = 'nocua@gmail.com',
            opinion = 'Test de opinion'
        )
        
        
    def test_charfields(self):
        self.assertIsInstance(self.formcomunicate.nombre, str)
        self.assertIsInstance(self.formcomunicate.correo, str)
    
    def test_charfields2(self):
        self.assertIsInstance(self.formcomunicate.opinion, str)
       
    