from django import forms
from .models import Clientes # pega os campos e cria um form

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )