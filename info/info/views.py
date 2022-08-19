from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def contacto(request):
    return render(request,'contacto.html')

def mision_vision(request):
    return render(request,'mision_vision.html')
