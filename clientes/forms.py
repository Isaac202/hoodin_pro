from django import forms
from .models import Clientes # pega os campos e cria um form
from indicacoes.models import Indicacao

class ClientesForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    confirma_senha = forms.CharField(widget=forms.PasswordInput, required=True)


    class Meta:
        model = Clientes
        fields = ['nome', 'email', 'telefone', 'celular', 'data_nascimento', 'sexo', 'tipo_pessoa', 'nome_mae',
                  'nome_pai', 'cnpjcpf', 'senha', 'confirma_senha', 'codindicacao_por' ]
        #colocar os campos que não quer que apareça
        exclude = ['id', 'codusuario', 'endereco_ok', 'dados_ok', 'codindicacao']


        def clean_confirma_senha(self):
            senha = self.cleaned_data.get("senha")
            confirma = self.clean_data.get("confirma_senha")
            if senha !=confirma:
                raise forms.ValidationError("Atenção senha difretne da confirmação")

            return senha

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if Clientes.objects.filter(email=email).exists():
                raise forms.ValidationError("Email Já cadastrado")

            return email


class BuscarForm(forms.Form):
    nome_cliente = forms.CharField(label='nome', max_length=80, required=False)
