from django import forms
from .models import Indicacoes # pega os campos e cria um form

class IndicacoesForm(forms.ModelForm):

    class Meta:
        model = Indicacoes
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )