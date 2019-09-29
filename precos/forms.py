from django import forms
from .models import Precos # pega os campos e cria um form
from servicos.models import Servicos

class PrecosForm(forms.ModelForm):

    class Meta:
        model = Precos
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

        class PrecosForm(forms.ModelForm):
            # no choices eu fiz um list comprehension que apenas gera um list [a,b,c...z] que vai ser renderizado no select
            servicos = forms.ChoiceField(
                choices=[('0', '--Selecione--')] + [(servicos.id, servicos.nome) for servicos in
                                                    Servicos.objects.all()])


class BuscarForm(forms.Form):
    nome_preco = forms.CharField(label='nome', max_length=80, required=False)
