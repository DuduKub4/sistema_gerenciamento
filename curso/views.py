from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_cursos.html', {'cursos': cursos})

def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'curso/adicionar_curso.html', {'form': form})

def remover_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')

    return redirect('listar_cursos')