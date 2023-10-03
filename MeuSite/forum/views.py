from django.shortcuts import render, get_object_or_404
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

#Update
class PublicacaoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        formulario = PublicacaoModel2Form(instance=publicacao)
        context = {'publicacao': formulario, }
        return render(request, 'forum/atualizaPublicacao.html', context)
   
    def post(self, request, pk, *args, **kwargs):
        publicacao = get_object_or_404(Publicacao, pk=pk)
        formulario = PublicacaoModel2Form(request.POST, instance=publicacao)
        if formulario.is_valid():
            publicacao = formulario.save() # cria uma pessoa com os dados do formulário
            publicacao.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("forum:lista-publicacoes"))
        else:
            contexto = {'publicacao': formulario, }
            return render(request, 'forum/atualizaPublicacao.html', contexto)


class PublicacaoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        contexto = { 'publicacao': publicacao, }
        return render(
            request, 'forum/apagaPublicacao.html',
            contexto)
    def post(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        publicacao.delete()
        return HttpResponseRedirect(
            reverse_lazy("forum:lista-publicacoes"))