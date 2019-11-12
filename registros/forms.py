from decimal import Decimal

from django import forms
from registros.models import Registros
from clientes.models import Clientes
from servicos.models import Servicos
from extensoes.models import Extensoes
from servicos_extensoes.models import Servicos_Extensoes


class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = [ 'codservico', 'codusuario', 'valor', 'arquivo', 'assinatura', 'versao',
                 'descricao', 'codqrcode', 'codindicacao', 'desconto', 'resumo_obra']
        exclude = ['data', 'assinatura', 'codcliente']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(RegistrosForm, self).__init__(*args, **kwargs)

    def clean(self):
        try:
            cli = Clientes.objects.filter(codusuario=self.user).first()
            saldo = Decimal(cli.valor_credito)
            servico_nome = self.cleaned_data.get('codservico')
            servi = Servicos.objects.filter(nome=servico_nome).frist()
            val_servico = Decimal(servi.preco)
            cod_servico = servi.id
            Servicos_Extensoes.objects.prefetch_related('Servico', 'Extensoes').filter(codservico=cod_servico).all()


            if saldo < val_servico:
                raise forms.ValidationError(
                   "a valor do servico maior que seu Saldo: " + str(saldo) +"coloque credito")
        except Exception as e:
            print(str(e))
        return self.cleaned_data







