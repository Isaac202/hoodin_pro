from django import forms
from .models import Servicos # pega os campos e cria um form

class ServicosForm(forms.ModelForm):

    class Meta:
        model = Servicos
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

class BuscarForm(forms.Form):
    nome_servico = forms.CharField(label='nome', max_length=80, required=False)


