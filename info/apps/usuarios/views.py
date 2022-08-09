from django.shortcuts import render

# Create your views here.
def Logearse(request):
    return render(request,'usuarios/Logearse.html')

def Registrarse(request):
    return render(request,'usuarios/Registrarse.html')