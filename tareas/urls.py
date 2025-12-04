from django.urls import path
from tareas import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tarea/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/nueva/', views.nueva_tarea, name='nueva_tarea'),
    path('tarea/eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tarea/toggle/<int:id>/', views.toggle_completada, name='toggle_tarea'),
    path('dashboard/', views.lista_tareas, name='dashboard'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
]