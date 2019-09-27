from django import forms
from .models import Clientes # pega os campos e cria um form
from indicacoes.models import Indicacoes

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

        class ClientesForm(forms.ModelForm):
            # no choices eu fiz um list comprehension que apenas gera um list [a,b,c...z] que vai ser renderizado no select
            indicacoes = forms.ChoiceField(
                choices=[('0', '--Selecione--')] + [(indicacao.codindicacao, indicacao.nome) for indicacao in
                                                    Indicacoes.objects.all()])