from os import path
from tareas import views


urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/nueva/', views.nueva_tarea, name='nueva_tarea'),
    path('tarea/eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
]