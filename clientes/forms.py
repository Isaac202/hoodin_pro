from django import forms
from .models import Clientes # pega os campos e cria um form
from indicacoes.models import Indicacoes
from pycpfcnpj import cpfcnpj
import re
from servicos.models import Servicos



class ClientesForm(forms.ModelForm):
   
    class Meta:
        model = Clientes
        # fields = ['nome', 'email', 'valor_credito', 'telefone', 'celular', 'data_nascimento', 'sexo',
        #            'tipo_pessoa', 'nome_mae', 'nome_pai', 'cnpjcpf', 'codindicacao', 'senha', 'confirma_senha',
        #            'cep', 'endereco', 'complemento', 'numero', 'pais', 'estado', 'cidade', 'bairro', 'documento_identidade',
        #            'documento_tipo', 'passaporte', 'nacionalidade', 'estadocivil', 'biografia', 'nif', 'facebook', 'twitter',
        #            'homepage', 'atuacao']
        #colocar os campos que não quer que apareça
        exclude = ['id', 'id_usuario', 'tipo_pessoa', 'valor_credito', 'codcliente', 'confirmation_key'] #'codindicacao',#, 'atuacao'


    def clean_cnpjcpf(self):

        cnpj = self.cleaned_data.get("cnpjcpf")
        masked_cnpj_number = cpfcnpj.clear_punctuation(cnpj)
        doc = "CPF"
        if len(cnpj) > 14:
            doc = "CNPJ"

        if cpfcnpj.validate(masked_cnpj_number) == False:
            raise forms.ValidationError("{} invalido!".format(doc))

        if Clientes.objects.filter(cnpjcpf=cnpj).exists():
            raise forms.ValidationError("{} Já cadastrado".format(doc))

        return cnpj

    def clean_cep(self):
        regexCep = re.compile('^[0-9]{5}-[\d]{3}$')
        data = self.cleaned_data.get("cep")
        if regexCep.match(data) is None:
            raise forms.ValidationError("Cep inválido.")
        return data


class ClienteUpdateForm(forms.ModelForm):

     class Meta:
        model = Clientes
        #colocar os campos que não quer que apareça
        exclude = ['nome' ,'id_usuario', 'passaporte','data_nascimento','nacionalidade',
            'nome_mae', "nome_pai", 'codindicacao', 'tipo_pessoa',
            'valor_credito', 'cnpjcpf','documento_tipo', 
            'documento_identidade', 'sexo' ,
            'codcliente', 'confirmation_key'] 



class BuscarForm(forms.Form):
    nome_cliente = forms.CharField(label='nome', max_length=80, required=False)



