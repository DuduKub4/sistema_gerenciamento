# curso/models.py
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome
