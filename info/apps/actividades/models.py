from django.db import models

# Create your models here.

class Animador(models.Model):
    nombre = models.CharField(max_length = 60) 
    zona = models.CharField(max_length = 60, null= True, blank = True) 

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to = 'actividades', null = True, blank=True)
    animador = models.ForeignKey(Animador, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.titulo