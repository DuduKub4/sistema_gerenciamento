from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aluno.urls')),  # Página inicial para alunos
    path('curso/', include('curso.urls')),
]
