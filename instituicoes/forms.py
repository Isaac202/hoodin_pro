from django import forms
from .models import Instituicoes # pega os campos e cria um form

class InstituicoesForm(forms.ModelForm):

    class Meta:
        model = Instituicoes
        #colocar os campos que não quer que apareça
        exclude = ['id']

class BuscarForm(forms.Form):
    nome_instituicao = forms.CharField(label='nome', max_length=80, required=False)
