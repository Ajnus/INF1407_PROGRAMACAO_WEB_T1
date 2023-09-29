from django.db import models

class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
    max_length=100, help_text='Entre o titulo')
    texto = models.CharField(
    max_length=10000, help_text='Digite o texto da publicacao')

def __str__(self):
    return self.titulo