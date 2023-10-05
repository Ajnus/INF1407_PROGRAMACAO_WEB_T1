from django.db import models

class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
    max_length=100, help_text='Entre o titulo')
    texto = models.CharField(
    max_length=10000, help_text='Digite o texto da publicacao')

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(
    max_length=100, help_text='Digite o comentario')
    idPublicacao  = models.ForeignKey(Publicacao,on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

