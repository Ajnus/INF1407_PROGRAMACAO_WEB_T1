from django import forms
from forum.models import Publicacao

class PublicacaoModel2Form(forms.ModelForm):


    class Meta:
        model = Publicacao
        fields = [
            'titulo',
            'texto',
        ]