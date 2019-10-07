from django import forms
from registros.models import Registros


class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = ['codcliente', 'codservico', 'valor', 'arquivo', 'assinatura', 'versao',
                 'descricao', 'codqrcode', 'codindicacao', 'desconto', 'resumo_obra']
        exclude = ['data', 'assinatura']





