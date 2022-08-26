from turtle import color
from django import forms


from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    Email = forms.EmailField(label='Correo',required=True)
    
    first_name = forms.CharField(label='',required=True)
    
    last_name = forms.CharField(label='Apellido', required=True)
    Clave = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    Clave2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'Email',
            'Clave',
            'Clave2',
        ]