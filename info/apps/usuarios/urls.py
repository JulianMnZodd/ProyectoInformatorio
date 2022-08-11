from django.urls import path
from . import views

app_name= 'usuarios'

urlpatterns = [
    path('ingresar/',views.Logearse, name='Logearse'),
    path('registrarse/',views.Registrarse, name='Registrarse'),
    path('index/',views.index, name='index'),
]