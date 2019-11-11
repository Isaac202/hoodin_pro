from decimal import Decimal

from django import forms
from registros.models import Registros
from clientes.models import Clientes
from servicos.models import Servicos

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = [ 'codservico', 'codusuario', 'valor', 'arquivo', 'assinatura', 'versao',
                 'descricao', 'codqrcode', 'codindicacao', 'desconto', 'resumo_obra']
        exclude = ['data', 'assinatura', 'codcliente']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(RegistrosForm, self).__init__(*args, **kwargs)
    ''' 
    def clean(self):
        cli = Clientes.objects.filter(codusuario=self.user).first()
        saldo = Decimal(cli.valor_credito)
        cod_servico = int(self.cleaned_data.get("codservico"))
        servi = Servicos.objects.filter(id=cod_servico).frist()
        val_servico = Decimal(servi.preco)

        if saldo < val_servico:
            raise forms.ValidationError(
                "a valor do servico maior que seu Saldo: " + str(saldo) +"coloque credito")

    '''





