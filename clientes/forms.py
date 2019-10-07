from django import forms
from .models import Clientes # pega os campos e cria um form
from indicacoes.models import Indicacao

class ClientesForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Clientes
        #colocar os campos que não quer que apareça
        exclude = ['id', 'codusuario']
        ''''
            indicacoes = forms.ChoiceField(
                choices=[('0', '--Selecione--')] + [(indicacao.id, indicacao.nome) for indicacao in
                                                    Indicacoes.objects.all()])
        '''

class BuscarForm(forms.Form):
    nome_cliente = forms.CharField(label='nome', max_length=80, required=False)
