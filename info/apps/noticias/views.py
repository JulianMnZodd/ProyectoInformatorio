from django.shortcuts import render
from .models import Noticia
# Create your views here.

def Listar(request):
    #Creo el diccionario para pasar datos al templeate
    ctx={}
    #Buscar las noticias de la BD
    todas=Noticia.objects.all()
    #Buscar lo que quiera de la BD
    ctx['notis']=todas
    
    return render(request,'noticias/listar_noticias.html',ctx)
#EJEMPLO DE COMO DESARMA EL CTX EL TEMPLETA
# ctx['nombre']='nicolas'