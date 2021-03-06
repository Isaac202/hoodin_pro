from django import forms
from django.db import models
from .models import Clientes  # pega os campos e cria um form
from indicacoes.models import Indicacoes
from pycpfcnpj import cpfcnpj
import re
from servicos.models import Servicos

ESTADOS_CHOICES = (
    ('--', '--'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

DISTRITOS_PORTUGAL_CHOICES = (
    ('--', '--'),
    ('Aveiro', 'Aveiro'),
    ('Beja', 'Beja'),
    ('Braga', 'Braga'),
    ('Bragança', 'Bragança'),
    ('Castelo Branco', 'Castelo Branco'),
    ('Coimbra', 'Coimbra'),
    ('Evora', 'Evora'),
    ('Faro', 'Faro'),
    ('Guarda', 'Guarda'),
    ('Leiria', 'Leiria'),
    ('Lisboa', 'Lisboa'),
    ('Portalegre', 'Portalegre'),
    ('Porto', 'Porto'),
    ('Santarem', 'Santarem'),
    ('Setubal', 'Setubal'),
    ('Viana do Castelo', 'Viana do Castelo'),
    ('Vila Real', 'Vila Real'),
    ('Viseu', 'Viseu')
)


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes

        exclude = ['id', 'id_usuario', 'tipo_pessoa', 'valor_credito', 'pontuacao',
                   'id_cliente', 'confirmation_key']  # 'codindicacao',#, 'atuacao'


                #self.fields['pais'].choices = Servicos.objects.filter(
                #servico_digitalizacao=sd)
        #estado = forms.ChoiceField(label='Share with groups', choices=)


    def clean_pais(self):
        data = self.data.get("pais")
        return data

    # estado = forms.ChoiceField(label='Share with groups', choices=DISTRITOS_PORTUGAL_CHOICES)

    # def __init__(self, *args, **kwargs):
    #    self.fields['estado'].empty_label = None
    #    self.fields['estado'].choices = self.DISTRITOS_PORTUGAL_CHOICES
    #    super(ClientesForm, self).__init__(*args, **kwargs)


    def clean_cnpjcpf(self):
        cnpj = " "
        pais = self.clean_pais()
        if pais == "BR":
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
        pais = self.clean_pais()
        if (regexCep.match(data) is None) & (pais == "BR"):
            raise forms.ValidationError("Cep inválido.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['atuacao'].queryset = Servicos.objects.filter(servico_digitalizacao=False)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                # 'placeholder': field.capitalize(),
                'class': 'form-control'
            })

def editable_fields(field):
    fields = ['celular', 'telefone', 'passaporte','nome_mae',"nome_pai", 'codigo_promocional',
              'biografia', 'nif', 'facebook', 'twitter', 'homepage', 'atuacao','estadocivil',
              'cep', 'endereco', 'complemento', 'numero', 'pais', 'estado', 'cidade', 'bairro']
    if field in fields:
        return True
    return False


class ClienteUpdateForm(forms.ModelForm):

    class Meta:
        model = Clientes
        # colocar os campos que não quer que apareça
        exclude = ['nome', 'id_usuario', 'data_nascimento', 'nacionalidade',
                  'codindicacao', 'tipo_pessoa',
                   'valor_credito', 'cnpjcpf', 'documento_tipo',
                   'documento_identidade', 'sexo', 'pontuacao',
        'id_usuario','id_cliente', 'confirmation_key','meu_link_indicacao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                # 'placeholder': field.capitalize(),
            })
            if not editable_fields(field):
                self.fields[field].widget.attrs['disabled'] = 'disabled'


class BuscarForm(forms.Form):
    nome_cliente = forms.CharField(label='nome', max_length=80, required=False)
