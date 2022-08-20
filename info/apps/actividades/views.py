from django.shortcuts import render

# Create your views here.

def Acts(request):
    return render(request,'actividades/listar_actividades.html')
