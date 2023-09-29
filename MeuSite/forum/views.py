from django.shortcuts import render
from forum.models import Publicacao
from django.views.generic.base import View
from forum.forms import PublicacaoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


class PublicacaoListView(View):
    def get(self, request, *args, **kwargs):
        publicacoes = Publicacao.objects.all()
        contexto = { 'publicacoes': publicacoes, }
        return render(
                request,
                'forum/listaPublicacoes.html',
                contexto)

class PublicacaoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': PublicacaoModel2Form, }
        return render(request,
            "forum/criaPublicacao.html", contexto)
    def post(self, request, *args, **kwargs):
        formulario = PublicacaoModel2Form(request.POST)
        if formulario.is_valid():
            publicacao = formulario.save()
            publicacao.save()
            return HttpResponseRedirect(reverse_lazy(
                "forum:lista-publicacoes"))