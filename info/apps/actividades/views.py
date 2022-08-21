from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Actividad
# Create your views here.

def Acts(request):
    ctx = {} 
    todas = Actividad.objects.all()
    print(todas) 
    ctx['acts'] = todas
    return render(request,'actividades/listar_actividades.html',ctx)

@login_required
def Detalle_Actividad(request,pk):
    ctx ={}
    actividad = Actividad.objects.get(pk=pk)
    ctx['resultado'] = actividad
    return render(request,'actividades/detalle_actividad.html',ctx)
