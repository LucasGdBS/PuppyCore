from django.db import models
# Create your models here.


class Tutor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    dataNascimento = models.DateField(max_length=10, blank=False)
    celular = models.CharField(max_length=13, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)

class Pet(models.Model):
    nomePet = models.CharField(max_length=50, null=False, blank=False)
    especie = models.CharField(max_length=20, null=False, blank=False)
    raca = models.CharField(max_length=20, null=False, blank=False)
    dtNasc = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, null=False, blank=False)
    peso = models.FloatField(max_length=5, null=True, blank=True)
    porte = models.CharField(max_length=20, null=False, blank=False)
    cadAtivo = models.BooleanField(default=True)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, default=1)

class CartaoVacina(models.Model):
    #nomePet = Pet.nomePet
    tipoVacina = models.CharField(max_length=30, null=False)
    dataVacina = models.DateField(null=True, blank=True)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, default=1)

