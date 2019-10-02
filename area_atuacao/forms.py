from django import forms
from .models import Area_Atuacao # pega os campos e cria um form

class Area_AtuacaoForm(forms.ModelForm):

    class Meta:
        model = Area_Atuacao
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

class BuscarForm(forms.Form):
    nome_area_atuacao = forms.CharField(label='nome', max_length=80, required=False)

