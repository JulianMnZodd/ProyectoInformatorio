from django.shortcuts import render

from apps.noticias.models import Noticia

def Home(request):
    ctx={}
    noticia=Noticia.objects.all().order_by('-creado')[:4]
    ctx['noticia']=noticia
    return render(request,'home.html',ctx)
    

def contacto(request):
    return render(request,'contacto.html')