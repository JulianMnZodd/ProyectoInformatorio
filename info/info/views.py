from django.shortcuts import render

from apps.noticias.models import Noticia
from apps.actividades.models import Actividad


def Home(request):
    noticia=Noticia.objects.all().order_by('-creado')[:3]
    actividad=Actividad.objects.all().order_by('-fecha')[:3]
    return render(request,'home.html',{'noticia':noticia,'actividad':actividad})

'''
def Home(request):
<<<<<<< HEAD
    noticia=Noticia.objects.all().order_by('-creado')[:3]
    actividad=Actividad.objects.all().order_by('-fecha')[:3]
    return render(request,'home.html',{'noticia':noticia,'actividad':actividad})
    
=======
    ctx={}
    noticia=Noticia.objects.all().order_by('-creado')[:4]
    ctx['noticia']=noticia
    return render(request,'home.html',ctx)    
'''
>>>>>>> b0243a487fe79dd3fdb8ab51cd23feb3057fb85c

def contacto(request):
    return render(request,'contacto.html')

def mision_vision(request):
    return render(request,'mision_vision.html')

def eventos(request):
    return render(request, 'eventos.html')
