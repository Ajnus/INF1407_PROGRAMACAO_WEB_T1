from django import forms
from forum.models import Publicacao, Comentario

class PublicacaoModel2Form(forms.ModelForm):


    class Meta:
        model = Publicacao
        fields = [
            'titulo',
            'texto',
        ]


class ComentarioModel2Form(forms.ModelForm):


    class Meta:
        model = Comentario
        fields = [
            'texto',
        ]