from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from tareas.forms import TareaForm
from tareas.models import Tarea

def home(request):
    return render(request, 'tareas/home.html')

# Vistas para autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'dashboard.html', {'error': 'Credenciales inválidas'})
    return render(request, 'tareas/login.html')

def logout_view(request):
    pass

def register_view(request):
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
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect('dashboard')
        print("Tarea no enviada, datos inválidos")
        print(form.errors)
    else:
        form = TareaForm()
    return render(request, 'tareas/nueva_tarea.html', {'form': form})   



@login_required
def eliminar_tarea(request, id):
    pass