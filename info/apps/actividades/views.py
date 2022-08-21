from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . models import Actividad
# Create your views here.

def Acts(request):

    ctx = {} 
    todas = Actividad.objects.all()
    print(todas) 
    ctx['acts'] = todas

    return render(request,'actividades/listar_actividades.html',ctx)
