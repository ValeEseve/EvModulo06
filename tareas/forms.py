from django import forms
from tareas.models import Tarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        error_messages = {
            "username": {
                "required": "El nombre de usuario es obligatorio.",
                "unique": "Este nombre ya está en uso.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].error_messages.update({
            "required": "Debes ingresar una contraseña.",
        })
        self.fields["password2"].error_messages.update({
            "required": "Debes confirmar la contraseña.",
            "password_mismatch": "Las contraseñas no coinciden.",
        })

        
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }