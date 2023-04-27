from django import forms
from .models import Tutor, Pet, CartaoVacina, CartaoExames


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


class tutorAltera(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = [
            'nome',
            'cpf',
            'dataNascimento',
            'celular',
            'email'
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
