from django import forms
from tareas.models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }