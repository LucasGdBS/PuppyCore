from django import forms
from .models import Tutor
from .models import Pet


class tutorCadastro(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = [
            'nome',
            'cpf',
            'dataNascimento',
            'celular',
            'email'
        ]


class petCadastro(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'nomePet',
            'especie',
            'raca',
            'dtNasc',
            'sexo',
            'peso',
            'porte',
            'cadAtivo',
        ]
