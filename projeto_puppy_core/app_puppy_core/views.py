from django.shortcuts import render

# Create your views here.

def cadastroTutor(request):
    return render(request, 'clinica/cadastroTutor.html')
