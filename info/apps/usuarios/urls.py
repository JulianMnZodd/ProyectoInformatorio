from django.urls import path
from . import views

from django.contrib.auth import views as auth

app_name= 'usuarios'

urlpatterns = [
    
    path('registrarse/',views.Registrarse, name='Registrarse'),
    path('index/',views.index, name='index'),
    path('login/',auth.LoginView.as_view(template_name='usuarios/Logearse.html'),name='Logearse'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    
]