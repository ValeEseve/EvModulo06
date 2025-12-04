from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from tareas.models import Tarea

def home(request):
    return render(request, 'tareas/home.html')

# Vistas para autenticación
def login_view(request):
    pass

def logout_view(request):
    pass



@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/dashboard.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id, usuario=request.user)
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

@login_required
def nueva_tarea(request):
    pass

@login_required
def eliminar_tarea(request, id):
    pass