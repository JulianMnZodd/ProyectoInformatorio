from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'actividades'

urlpatterns = [
    path('listar/', views.Acts, name = 'listar_actividades'),

]

