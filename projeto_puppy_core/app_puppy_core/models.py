from django.db import models

# Create your models here.


class Tutor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.IntegerField(max_length=14, unique=True, null=False, blank=False)
    dataNascimento = models.DateField(max_length=10, blank=False)
    celular = models.IntegerField(max_length=13, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)

    
