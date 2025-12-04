from django import forms
from tareas.models import Tarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }