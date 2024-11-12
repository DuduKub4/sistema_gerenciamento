from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/listar_alunos.html', {'alunos': alunos})

def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'aluno/adicionar_aluno.html', {'form': form})
