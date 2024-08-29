
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarefas
from django.urls import reverse_lazy



##Ferramentas para login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from .forms import MeuCadastroForm, MeuLoginForm


# Create your views here.
class TarefasListView(ListView):
    model = Tarefas

class TarefasCreateView(CreateView):
    model = Tarefas
    fields = ["data", "responsavel", "tarefa", "status", "observacao"]
    success_url = reverse_lazy('tarefas_list')

class TarefasUpdateView(UpdateView):
    model = Tarefas
    fields = ["data", "responsavel", "tarefa", "status", "observacao"]
    template_name = 'cadastro/tarefas_form.html'
    success_url = reverse_lazy('tarefas_list')

class TarefasDeleteView(DeleteView):
    model = Tarefas
    template_name = 'lista/tarefas_delete.html'
    success_url = reverse_lazy('tarefas_list')

def sobre(request):
    return render(request, 'cadastro/sobre.html')


##Classe de login
class MeuLoginView(LoginView):
    template_name = 'cadastro/login.html'
    form_class = MeuLoginForm
    redirect_authenticated_user = True  # Redireciona usuários logados para a página principal
    success_url = reverse_lazy('alunos_list')  # Página para onde o usuário será redirecionado após o login


class MeuCadastroView(View):
    form_class = MeuCadastroForm
    initial = {'key': 'value'}
    template_name = 'cadastro/cadastro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a tela de login após o cadastro

        return render(request, self.template_name, {'form': form})

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

