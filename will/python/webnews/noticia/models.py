from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(default="1980-01-01")
    email = models.EmailField(default='exemplo@exemplo.com.br')
    idade = models.PositiveSmallIntegerField(default='1')

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.DateField(default="1980")
    diretor = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=500)
    capa = models.ImageField(upload_to='filmes/', null=True, blank=True)

    def __str__(self):
        return self.titulo