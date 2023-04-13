from django.shortcuts import render

from .models import Tutor
from .forms import tutorCadastro, petCadastro , vacinaCadastro
from .models import Pet
from .models import CartaoVacina


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

def cadastroPet(request):
    if request.method == 'POST':
        form = petCadastro(request.POST)
        if form.is_valid():
            pet = Pet(**form.cleaned_data)

            pet.save()
            return render(request, 'clinica/sucessocadastro.html')
        else: 
            return render(request, 'clinica/falhacadastro.html')
    else:   
        form = petCadastro()
        return render(request, 'clinica/cadastroPet.html', {'form': form})

def cartaoVacina(request):

    return render(request, 'tutor/verVacina.html')

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


