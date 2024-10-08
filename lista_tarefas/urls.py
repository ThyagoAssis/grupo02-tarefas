from django.contrib import admin
from django.urls import path

from cadastro.views import TarefasListView, TarefasCreateView, TarefasUpdateView, TarefasDeleteView, sobre, SolicitarDadosView, EncerrarSessaoView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', TarefasListView.as_view(), name='tarefas_list'),
    path('cadastro/', TarefasCreateView.as_view(), name='tarefas_form'),
    path('edicao/<int:pk>/', TarefasUpdateView.as_view(), name='tarefas_edicao'),
    path('delete/<int:pk>/', TarefasDeleteView.as_view(), name='tarefas_delete'),
    path('sobre/', sobre, name='sobre'),


#Section
    path("", SolicitarDadosView.as_view(), name='section'),
    path("encerra_sessao", EncerrarSessaoView.as_view(), name='section_fim')
]

    #Rotas de login


    #path('', MeuLoginView.as_view(), name='login'),
    #path('cadastro_login/', MeuCadastroView.as_view(), name='cadastro_login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


#path('', tarefas_form.as_view(), name='tarefas_form'),
#path('about/', name='tarefas_list', tarefas_list.as_view()),