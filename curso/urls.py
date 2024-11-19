from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),
    path('remover_curso/<int:id>/', views.remover_curso, name='remover_curso'),
]
