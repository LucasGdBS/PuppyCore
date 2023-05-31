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
    dtNasc = models.DateField(null=True, blank=True, default=0000-00-00)
    sexo = models.CharField(max_length=1, null=False, blank=False)
    peso = models.FloatField(max_length=5, null=True, blank=True)
    porte = models.CharField(max_length=20, null=False, blank=False)
    cadAtivo = models.BooleanField(default=True)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)


class CartaoVacina(models.Model):
    nomeVeterinario = models.CharField(max_length=100, null=False)
    dataVacina = models.DateField(null=False, blank=True)
    tipoVacina = models.CharField(max_length=30, null=False)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)


class CartaoExames(models.Model):
    exame = models.CharField(max_length=100, null=False)
    nomeVeterinario = models.CharField(max_length=100, null=False)
    dataSolicitacao = models.DateField(null=False, blank=False)
    dataResultado = models.DateField(null=False, blank=True)
    resultado = models.CharField(max_length=500, null=False)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, default=1)

class Login(models.Model):
    cpf = models.CharField(max_length=11, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False)

class Vacinacao(models.Model):
    nomeVacina = models.CharField(max_length=100, null=False)
    dataVacina = models.DateField(null=False, blank=False)
    vetResponsavel = models.CharField(max_length=100, null=False)
