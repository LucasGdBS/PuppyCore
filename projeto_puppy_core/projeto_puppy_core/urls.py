from django.urls import path
from app_puppy_core import views

urlpatterns = [
    path('cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor'),
    path('falhacadastro/', views.falhacadastro, name='Falha Cadastro'),

    # puppycore.com
    # puppycore.com/cadastroTutor/ 
    # NÃO ESQUECER DA BARRA /
]
