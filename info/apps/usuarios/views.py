from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm


# Create your views here.


class Registrarse(CreateView):
    form_class = RegistroForm 
    
    success_url = reverse_lazy('usuarios:Logearse')
	
    template_name = 'usuarios/Registrarse.html'

    

# Create your views here.
def Logearse(request):
    return render(request,'usuarios/Logearse.html')



