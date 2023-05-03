from django.urls import path
from app_puppy_core import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'),
    path('cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor'),
    path('falhacadastro/', views.falhacadastro, name='Falha Cadastro'),
    path('sucessocadastro/', views.sucessocadastro, name='Sucesso Cadastro'),
    path('cadastroPet/<pk>/', views.cadastroPet, name='Cadastro Pet'),
    path('cartaoVacinas/', views.cartaoVacina, name='Visualizar Vacinas'),
    path('cadastroVacinas/', views.cadastroVacina, name='Cadastrar Vacinas'),
    path('homeAdm/', views.homeAdm, name='Home do Administrador'),
    path('homeTutor/', views.homeTutor, name='Home do Tutor'),
    path('homeAdm/infoTutor/<pk>/', views.infoTutor, name='Info Tutor'),
    path('login/', views.login, name='Login'),
    path('infoPets/', views.infoPets, name='Info Pets'),
    

    
    # puppycore.com
    # puppycore.com/cadastroTutor/ 
    # NÃO ESQUECER DA BARRA / E DA VÍRGULA
]
