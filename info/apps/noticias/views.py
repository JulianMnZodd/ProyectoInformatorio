from datetime import date
from symtable import Class
from django.shortcuts import render
from .models import Noticia
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def Listar(request):
    #Creo el diccionario para pasar datos al templeate
    #ctx={}
    #Buscar las noticias de la BD
    todas=Noticia.objects.all()
    #Buscar lo que quiera de la BD
    #ctx['notis']=todas
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})
    #return render(request,'noticias/listar_noticias.html',ctx)

def ListarporFecha(request):
    todas=Noticia.objects.all().order_by('-creado')
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})


#def MostrarNoticia(request):
    #ctx={}
    #noticia=Noticia.objects.all()
    #ctx['noticia']=noticia
    #return render(request,'noticias/Pag_Noticia.html',ctx)
    
class DetalleNoticia(LoginRequiredMixin,DetailView):
    model=Noticia
    template_name='noticias/Detalle_Noticia.html'
    
    