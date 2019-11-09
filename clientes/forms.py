from django import forms
from .models import Clientes # pega os campos e cria um form
from indicacoes.models import Indicacoes
from pycpfcnpj import cpfcnpj
import re
from servicos.models import Servicos



class ClientesForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    confirma_senha = forms.CharField(widget=forms.PasswordInput, required=True)
    '''atuacao = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Servicos.objects.all()
               )
    '''


    class Meta:
        model = Clientes
        fields = ['nome', 'email', 'valor_credito', 'telefone', 'celular', 'data_nascimento', 'sexo',
                   'tipo_pessoa', 'nome_mae', 'nome_pai', 'cnpjcpf', 'codindicacao', 'senha', 'confirma_senha',
                   'cep', 'endereco', 'complemento', 'numero', 'pais', 'estado', 'cidade', 'bairro', 'documento_identidade',
                   'documento_tipo', 'passaporte', 'nacionalidade', 'estadocivil', 'biografia', 'nif', 'facebook', 'twitter',
                   'homepage', 'atuacao']
        #colocar os campos que não quer que apareça
        exclude = ['id', 'codusuario', 'codcliente', 'confirmation_key']
#'codindicacao',
#, 'atuacao'

    def clean_confirma_senha(self):
        senha = self.cleaned_data.get("senha")
        confirma = self.cleaned_data.get("confirma_senha")
        if senha != confirma:
            raise forms.ValidationError("Atenção senha difretne da confirmação")

        return senha

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Clientes.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Já cadastrado")

        return email

    def clean_cnpjcpf(self):

        cnpj = self.cleaned_data.get("cnpjcpf")
        masked_cnpj_number = cpfcnpj.clear_punctuation(cnpj)

        if cpfcnpj.validate(masked_cnpj_number) == False:
            raise forms.ValidationError("documento invalido")

        return cnpj

    def clean_cep(self):
        regexCep = re.compile('^[0-9]{5}-[\d]{3}$')
        data = self.cleaned_data.get("cep")
        if regexCep.match(data) is None:
            raise forms.ValidationError("Cep inválido.")
        return data


class BuscarForm(forms.Form):
    nome_cliente = forms.CharField(label='nome', max_length=80, required=False)



