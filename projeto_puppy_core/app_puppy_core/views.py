from django.shortcuts import render
from .forms import tutorCadastro
from .models import Tutor

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



