from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),
]
