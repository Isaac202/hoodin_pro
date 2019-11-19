from django import forms
from .models import Extensoes # pega os campos e cria um form

class ExtensoesForm(forms.ModelForm):

    class Meta:
        model = Extensoes
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

class BuscarForm(forms.Form):
    nome_extensao = forms.CharField(label='nome', max_length=80, required=False)

