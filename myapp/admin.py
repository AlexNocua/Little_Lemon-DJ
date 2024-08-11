from django.contrib import admin
from .models import Reservation, ReservationAdmin, Menu, MenuForm,FormComunicate, FormComunicateAdmin
# Register your models here.
# impotrtacion de modelos para denterizado de HTML
from django.utils.html import format_html

# importacion para la renderizacion de la imagen en base 64
import base64


admin.site.register(FormComunicate,FormComunicateAdmin)

admin.site.register(Reservation, ReservationAdmin)

# esta es una forma de registrar los modelos creados
# admin.site.register(Menu, MenuAdmin)

# otra forma para registrar los modelo para la visualizar la imagen
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ('nombreproducto', 'cantidad_producto', 'mostrar_imagen')

    def mostrar_imagen(self, obj):
        if obj.imagen:
            # Codificar la imagen binaria en Base64
            imagen_64 = base64.b64encode(obj.imagen).decode('utf-8')
            return format_html('<img src="data:image/jpeg;base64,{0}" width="50" height="50" />', imagen_64)
        return 'No hay imagen'

    mostrar_imagen.short_description = 'Imagen'
