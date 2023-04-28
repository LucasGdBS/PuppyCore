from django.shortcuts import render

from .models import Tutor
from .forms import tutorCadastro, petCadastro, vacinaCadastro
from .models import Pet
from .models import CartaoVacina
from .models import CartaoExames

# Create your views here.


def cadastroTutor(request):
    if request.method == 'POST':
        form = tutorCadastro(request.POST)
        if form.is_valid():
            tutor = Tutor(**form.cleaned_data)

            tutor.save()
            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
    else:
        form = tutorCadastro()
        return render(request, 'clinica/cadastroTutor.html', {'form': form})


def falhacadastro(request):
    return render(request, 'clinica/falhacadastro.html')


def sucessocadastro(request):
    return render(request, 'clinica/sucessocadastro.html')


def home(request):
    return render(request, 'clinica/home.html')


def cadastroPet(request, pk:int):
    if request.method == 'POST':
        form = petCadastro(request.POST)
        if form.is_valid():
            pet = Pet(tutor = Tutor(id=pk), **form.cleaned_data)
            

            pet.save()
            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
    else:
        form = petCadastro()
        return render(request, 'clinica/cadastroPet.html', {'form': form, 'pk': pk})


def cartaoVacina(request):
    dados = CartaoVacina.objects.all()

    context = {
        'nomePet': 'Tinker Bell',
        'dados': dados,
    }

    return render(request, 'tutor/verVacinas.html', context)


def cadastroVacina(request):
    if request.method == 'POST':
        form = vacinaCadastro(request.POST)
        if form.is_valid():
            cartaoVacina = CartaoVacina(**form.cleaned_data)

            cartaoVacina.save()
            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
    else:
        form = vacinaCadastro()
        return render(request, 'clinica/cadastroVacina.html', {'form': form})


def homeAdm(request):
    tutor = Tutor.objects.all()

    context = {
        'tutor': tutor
    }

    return render(request, 'clinica/homeAdm.html', context)


def homeTutor(request):
    return render(request, 'tutor/homeTutor.html')

def cadastroExames(request):
    if request.method == 'POST':
        form = cadastroExames(request.POST)
        if form.is_valid():
            CartaoExames = CartaoExames(**form.cleaned_data)

            CartaoExames.save()
            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
    else:
        form = cadastroExames()
        return render(request, 'clinica/cadastroExames.html', {'form': form})
    
def infoTutor(request, pk:int):
    if request.method == 'GET':
        tutor = Tutor.objects.get(pk=pk)
        return render(request, 'clinica/infoTutor.html', context = {'tutor': tutor})
