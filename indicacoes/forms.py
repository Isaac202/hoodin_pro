from django import forms
from .models import Indicacoes # pega os campos e cria um form

class IndicacoesForm(forms.ModelForm):

    class Meta:
        model = Indicacoes
        #colocar os campos que não quer que apareça
        exclude = ['id']

class BuscarForm(forms.Form):
    nome_indicacao = forms.CharField(label='nome', max_length=80, required=False)
