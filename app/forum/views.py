from django.shortcuts import render, get_object_or_404
from forum.models import Publicacao,Comentario
from django.views.generic.base import View
from forum.forms import PublicacaoModel2Form, ComentarioModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class PublicacaoView(View):
    def get(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        comentarios = Comentario.objects.filter(idPublicacao=pk)
        user = request.user
        contexto = { 'publicacao': publicacao, 'comentarios':comentarios, 'user':user}
        return render(
                request,
                'forum/visualizaPublicacao.html',
                contexto)
    #CreateComentario
    def post(self, request, pk, *args, **kwargs):
    
        comentario_texto = request.POST.get("comentario_nome")

        publicacao = Publicacao.objects.get(pk=pk)
        novo_comentario = Comentario(texto=comentario_texto, autor=request.user,idPublicacao =publicacao)

        novo_comentario.save()

        return self.get(request=request, pk = pk)

@method_decorator(login_required, name='dispatch')
class PublicacaoListView(View):
    def get(self, request, *args, **kwargs):
        publicacoes = Publicacao.objects.all()
        contexto = { 'publicacoes': publicacoes, 'user':request.user}
        return render(
                request,
                'forum/listaPublicacoes.html',
                contexto)


@method_decorator(login_required, name='dispatch')
class PublicacaoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': PublicacaoModel2Form, }
        return render(request,
            "forum/criaPublicacao.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = PublicacaoModel2Form(request.POST)
        if formulario.is_valid():
            publicacao = formulario.save(commit=False)  
            publicacao.autor = request.user
            publicacao.save()
            return HttpResponseRedirect(reverse_lazy(
                "forum:lista-publicacoes"))

@method_decorator(login_required, name='dispatch')
class PublicacaoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        if publicacao.autor == request.user:
            formulario = PublicacaoModel2Form(instance=publicacao)
            context = {'publicacao': formulario, }
            return render(request, 'forum/atualizaPublicacao.html', context)
        else:
            return HttpResponseRedirect(reverse_lazy(
                    "forum:lista-publicacoes"))


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


@method_decorator(login_required, name='dispatch')
class PublicacaoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        if publicacao.autor == request.user:
            contexto = { 'publicacao': publicacao, }
            return render(
                request, 'forum/apagaPublicacao.html',
                contexto)
        else:
            return HttpResponseRedirect(reverse_lazy(
                    "forum:lista-publicacoes"))

    def post(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        if publicacao.autor == request.user:
            publicacao.delete()
        return HttpResponseRedirect(
            reverse_lazy("forum:lista-publicacoes"))

@method_decorator(login_required, name='dispatch')
class ComentarioDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        comentario = Comentario.objects.get(pk=pk)
        publicacao = comentario.idPublicacao
        if comentario.autor == request.user:
            contexto = { 'publicacao': publicacao,'comentario': comentario, }
            return render(
                request, 'forum/apagaComentario.html',
                contexto)
        else:
            return HttpResponseRedirect(
            reverse_lazy("forum:ve-publicacao", kwargs={'pk': publicacao.id}))

    def post(self, request, pk, *args, **kwargs):
        comentario = Comentario.objects.get(pk=pk)
        publicacao = comentario.idPublicacao
        if comentario.autor == request.user:
            comentario.delete()
        return HttpResponseRedirect(
            reverse_lazy("forum:ve-publicacao", kwargs={'pk': publicacao.id}))




