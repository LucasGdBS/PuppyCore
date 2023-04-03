from django.contrib import admin
from django.urls import path
from app_puppy_core import views

urlpatterns = [
    path('cadastroTutor/', views.cadastroTutor, name='Cadastro Tutor')
]
