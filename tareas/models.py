from django.db import models



# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, default='General')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    prioridad = models.IntegerField(default=1)
    color_etiqueta = models.CharField(max_length=7, default='#FFFFFF')
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo