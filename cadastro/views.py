from django.views.generic import ListView, CreateView
from .models import Tarefas
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
class TarefasListView(ListView):
    model = Tarefas



class TarefasCreateView(CreateView):
    model = Tarefas

    fields = ["data", "responsavel", "tarefa", "status", "observacao"]

    success_url = reverse_lazy('tarefas_list')


# def index(request):
#     return render(request, 'tarefas_form.html')
#
# def about(request):
#     return render(request, 'tarefas_list.html')
#
#
# def Schedule(request):
#     return render(request, 'base.html')



#lass CadastroListView(ListView):
    #model = Cadastro

#class CadastroCreateView(CreateView):
   #model = Cadastro

