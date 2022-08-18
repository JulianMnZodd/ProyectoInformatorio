
from django.urls import path
from . import views

app_name='noticias'

urlpatterns = [
    path('listar/', views.Listar, name='listar_noticias'),
    path('listarPorFecha/', views.ListarporFecha, name='listar_noticiasporFecha'),
    path('MostrarNoticia/<int:pk>/', views.DetalleNoticia.as_view(), name='MostrarNoticia'),
]