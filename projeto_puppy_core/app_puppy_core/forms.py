from django import forms
from .models import Tutor, Pet, CartaoVacina, CartaoExames, Login, Vacinacao


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


class vacinaCadastro(forms.ModelForm):
    class Meta:
        model = CartaoVacina
        fields = [
            # 'nomePet',
            'nomeVeterinario',
            'dataVacina',
            'tipoVacina',
        ]

class cadastroExames(forms.ModelForm):
    class Meta:
        model = CartaoExames
        fields = [
            'exame',
            'dataSolicitacao',
            'dataResultado',
            'resultado',
            'nomeVeterinario'
        ]

class formLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'cpf',
            'senha'
        ]

class marcarVacina(forms.ModelForm):
    class Meta:
        model = Vacinacao
        fields = [
            'nomeVacina',
            'dataVacina',
            'vetResponsavel'
        ]
