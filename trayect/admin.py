from django.contrib import admin

from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona

# Register your models here.
admin.site.register(Persona)

admin.site.register(Ciudad)
admin.site.register(Indicador)
admin.site.register(CiudIndic)
admin.site.register(Antena)
admin.site.register(AntIndic)
admin.site.register(Estadia)
admin.site.register(Desplazamiento)

