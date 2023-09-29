from django.shortcuts import render
from forum.models import Publicacao
from django.views.generic.base import View

class PublicacaoListView(View):
    def get(self, request, *args, **kwargs):
        publicacoes = Publicacao.objects.all()
        contexto = { 'publicacoes': publicacoes, }
        return render(
                request,
                'forum/listaPublicacoes.html',
                contexto)