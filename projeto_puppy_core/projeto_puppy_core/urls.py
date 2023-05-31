from django.urls import path
from app_puppy_core import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),

    path('login/', views.login, name='Login'),

    path('homeAdm/', views.homeAdm, name='Home do Administrador'),

    path('homeAdm/cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor'),
    path('homeAdm/infoTutor/<pk>/alteracaoTutor/', views.alteracaoTutor, name='Alteracao Tutor'),
    path('homeAdm/infoTutor/<pk>/', views.infoTutor, name='Info Tutor'),
    path('homeAdm/infoTutor/<pk>/cadastroPet/', views.cadastroPet, name='Cadastro Pet'),
    path('homeAdm/infoTutor/<pk>/infoPet/<id_pet>/',views.infoPets, name='Info Pets'),
    path('homeAdm/infoTutor/<pk>/infoPet/<id_pet>/cadastroexames/', views.cadastrarExames, name='Cadastro Exames'),  # Falta implementar
    path('homeAdm/infoTutor/<pk>/infoPet/<id_pet>/cadastroVacinas/', views.cadastroVacina, name='Cadastrar Vacinas'),  # Falta implementar
    path('homeAdm/infoTutor/<pk>/infoPet/<id_pet>/cartaoVacinas/', views.cartaoVacinaAdm, name='Visualizar Vacinas'),

    path('homeTutor/', views.homeTutor, name='Home do Tutor'),
    path('homeTutor/cartaoVacinas/', views.cartaoVacina, name='Visualizar Vacinas'),
    path('marcarVacina/', views.vacinar, name='Marcar Vacina'),
    path('homeAdm/infoTutor/<pk>/infoPet/<id_pet>/cartaoExames/', views.cartaoExames, name='Visualizar Exames'),

    # puppycore.com
    # puppycore.com/cadastroTutor/
    # NÃO ESQUECER DA BARRA / E DA VÍRGULA
]
