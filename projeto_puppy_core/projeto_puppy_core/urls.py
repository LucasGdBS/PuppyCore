from django.urls import path
from app_puppy_core import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),

    path('login/', views.login, name='Login'),

    path('homeAdm/', views.homeAdm, name='Home do Administrador'),

    path('homeAdm/cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor'),
    path('homeAdm/infoTutor/<pk>/', views.infoTutor, name='Info Tutor'),
    path('homeAdm/infoTutor/<pk>/cadastroPet/', views.cadastroPet, name='Cadastro Pet'),
    path('homeAdm/infoPet/', views.infoPets, name='Info Pets'),
    path('homeAdm/cadastroexames/', views.cadastrarExames, name='Cadastro Exames'),
    path('homeAdm/cadastroVacinas/', views.cadastroVacina, name='Cadastrar Vacinas'),

    path('homeTutor/', views.homeTutor, name='Home do Tutor'),
    path('homeTutor/cartaoVacinas/', views.cartaoVacina, name='Visualizar Vacinas'),
    
    

    path('falhacadastro/', views.falhacadastro, name='Falha Cadastro'),
    path('sucessocadastro/', views.sucessocadastro, name='Sucesso Cadastro'),

    # puppycore.com
    # puppycore.com/cadastroTutor/ 
    # NÃO ESQUECER DA BARRA / E DA VÍRGULA
]
