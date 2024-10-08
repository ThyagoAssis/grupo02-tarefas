from django.db import models
from datetime import datetime

class Tarefas(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluida', 'Concluída'),
    ]

    tarefa = models.CharField(max_length=50, null=False, blank=False)
    observacao = models.CharField(max_length=240, null=False, blank=False)
    data = models.DateField()
    responsavel = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendente', null=False, blank=False)

class Login(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=10, null=False, blank=False)