from decimal import Decimal

from django import forms
from registros.models import Registros, ArquivoRegistro
from clientes.models import Clientes
from servicos.models import Servicos
from extensoes.models import Extensoes
from servicos_extensoes.models import Servicos_Extensoes


class RegistrosViewForm(forms.ModelForm):

    class Meta:
        model = Registros
        exclude = ['data', 'codregistro', 'arquivo', 'descricao',
                   'id_cliente', 'id_usuario', 'valor', 'desconto','manter_arquivo']

    def __init__(self, sd=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codservico'].queryset = Servicos.objects.filter(
            servico_digitalizacao=sd)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class RegistrosForm(forms.ModelForm):
    
    class Meta:
        model = Registros
        exclude = ['data', 'codregistro', 'arquivo', 'descricao',
                   'id_cliente', 'id_usuario', 'valor', 'desconto']



class ArquivoRegistroForm(forms.ModelForm):

    class Meta:
        model = ArquivoRegistro
        fields = ("file",)


