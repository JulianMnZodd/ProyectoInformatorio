from django.contrib import admin

# Register your models here.

from . models import Actividad,Animador

admin.site.register(Actividad)
admin.site.register(Animador)