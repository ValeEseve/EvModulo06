from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    # Se establecen las opciones de prioridad para las tareas
    PRIORIDAD_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
        (4, 'Urgente'),
    ]
    # Llamar al modelo User para relacionar cada tarea con un usuario específico
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')
    
    # Atributos de cada tarea
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, default='General')
    #fechas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)

    prioridad = models.IntegerField(default=1, choices=PRIORIDAD_CHOICES)
    color_etiqueta = models.CharField(max_length=7, default='#FFFFFF')
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo