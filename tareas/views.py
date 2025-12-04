from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tareas.models import Tarea


# Vistas Auth
def home(request):
    return render(request, 'tareas/dashboard.html')



@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, id):
    pass

@login_required
def nueva_tarea(request):
    pass

@login_required
def eliminar_tarea(request, id):
    pass