from django.urls import path
from app_puppy_core import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor'),
    path('falhacadastro/', views.falhacadastro, name='Falha Cadastro'),
    path('sucessocadastro/', views.sucessocadastro, name='Sucesso Cadastro'),

    # puppycore.com
    # puppycore.com/cadastroTutor/ 
    # NÃO ESQUECER DA BARRA /
]
