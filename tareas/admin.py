from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Tarea.
    """
    list_display = ['titulo', 'usuario', 'categoria', 'prioridad', 'completada', 
                    'fecha_creacion', 'fecha_vencimiento']
    list_filter = ['completada', 'prioridad', 'categoria', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion', 'categoria']
    list_editable = ['completada', 'prioridad']
    ordering = ['-fecha_creacion']
    date_hierarchy = 'fecha_creacion'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('usuario', 'titulo', 'descripcion')
        }),
        ('Clasificación', {
            'fields': ('categoria', 'prioridad', 'color_etiqueta')
        }),
        ('Fechas', {
            'fields': ('fecha_vencimiento',)
        }),
        ('Estado', {
            'fields': ('completada',)
        }),
    )
    
    readonly_fields = ['fecha_creacion']
    
    def get_queryset(self, request):
        """Personaliza el queryset según el usuario"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)