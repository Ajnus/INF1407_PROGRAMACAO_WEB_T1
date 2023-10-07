from django.shortcuts import render
from django.shortcuts import redirect
from app.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth import login


class AppUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
                return redirect('sec-home')

def homeSec(request):
    return redirect('forum:lista-publicacoes')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,
        'registro/registro.html', context)

@login_required
def logado(request):
    return redirect('forum:lista-publicacoes')


def home(request):
    return redirect('forum:lista-publicacoes')