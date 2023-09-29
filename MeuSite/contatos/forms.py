from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data do nascimento',
        help_text='Nascimento no formato DD/MM/AAAA',
    )
    class Meta:
        model = Pessoa
        fields = [
                'nome',
                'idade',
                'salario',
                'dtNasc'
                 ]
