from django.shortcuts import render, get_object_or_404

from .models import Tutor, Pet, CartaoExames, CartaoVacina, Vacinacao
from .forms import tutorCadastro, petCadastro, vacinaCadastro, formLogin, cadastroExames, marcarVacina

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


def home(request):
    return render(request, 'clinica/home.html')


def cadastroPet(request, pk: int):
    if request.method == 'POST':
        form = petCadastro(request.POST)
        if form.is_valid():
            pet = Pet(tutor=Tutor(id=pk), **form.cleaned_data)

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


def cadastroVacina(request, pk: int, id_pet: int):
    if request.method == 'POST':
        form = vacinaCadastro(request.POST)
        if form.is_valid():
            cartaoVacina = CartaoVacina(pet=Pet(id=id_pet), **form.cleaned_data)

            cartaoVacina.save()
            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
    else:
        form = vacinaCadastro()
        return render(request, 'clinica/cadastroVacina.html', {'form': form, 'pk': pk, 'id_pet' : id_pet})


def homeAdm(request):
    tutor = Tutor.objects.all()

    context = {
        'tutor': tutor
    }

    return render(request, 'clinica/homeAdm.html', context)


def homeTutor(request):
    return render(request, 'tutor/homeTutor.html')


def cadastrarExames(request):
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


def infoTutor(request, pk: int):
    if request.method == 'GET':
        tutor = Tutor.objects.get(pk=pk)
        idtutor = get_object_or_404(Tutor, pk=pk)
        pets = idtutor.pet_set.all()

        context = {
            'pets': pets,
            'tutor': tutor,
        }

        # itens = Item.objects.filter(usuario=request.user)

        return render(request, 'clinica/infoTutor.html', context)


def login(request):
    if request.method == 'POST':
        form = formLogin(request.POST)
        if form.is_valid():
            Login = Login(**form.cleaned_data)

            formLogin.save()
            return render(request, 'clinica/homeAdm.html')
        else:
            return render(request, 'geral/login.html')
    else:
        form = formLogin()
        return render(request, 'geral/login.html', {'form': form})


def infoPets(request, pk: int, id_pet: int):
    pet = Pet.objects.get(pk=id_pet)

    context = {
        'pet': pet,
    }

    return render(request, 'clinica/infoPets.html', context)


def alteracaoTutor(request, pk: int):
    if request.method == 'GET':
        tutor = Tutor.objects.get(pk=pk)
        form = tutorCadastro(instance=tutor)

        return render(request, template_name='clinica/alteracaoTutor.html', context={'form': form})
    
    elif request.method == 'POST':
        tutor = Tutor.objects.get(pk=pk)
        form = tutorCadastro(request.POST,instance=tutor)

        if form.is_valid():

            form.save()

            return render(request, 'clinica/sucessocadastro.html')
        else:
            return render(request, 'clinica/falhacadastro.html')
        
def cartaoVacinaAdm(request, pk: int, id_pet: int):
    if request.method == 'GET':
        idpet = get_object_or_404(Pet, pk=id_pet)
        vacinas = idpet.cartaovacina_set.all()

    context = {
        'dados': vacinas,
        'pk': pk,
        'id_pet': id_pet

    }


    return render(request, 'tutor/verVacinas.html', context)


def vacinar(request):
    if request.method == 'POST':
        form = marcarVacina(request.POST)
        if form.is_valid():
            Vacinacao = Vacinacao(**form.cleaned_data)

            Vacinacao.save()
            return render(request, 'clinica/sucessocadastro.html') #mudar a pagina que é redirecionada
        else:
            return render(request, 'clinica/falhacadastro.html') #mudar a pagina que é redirecionada
    else:
        form = marcarVacina()
        return render(request, 'clinica/cadastroExames.html', {'form': form}) #mudar a pagina que é redirecionada
        
