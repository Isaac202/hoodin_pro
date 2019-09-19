from django import forms
from .models import Indicacoes

class IndicacoesForm(forms.ModelForm):

    class Meta:
        model = Indicacoes
        fields = ['codindicacao', 'nome', 'percentual']



class BuscaForm(forms.Form):
    busca = forms.CharField(label='Nome', max_length=80, required=False)

