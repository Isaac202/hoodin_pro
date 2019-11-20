from django import forms
from .models import Clientes_Atuacao # pega os campos e cria um form


class ClientesAtuacaoForm(forms.ModelForm):

    class Meta:
        model = Clientes_Atuacao
        fields = ['id_cliente', 'codatuacao', 'codservico']
        #colocar os campos que não quer que apareça
        exclude = ['id']
