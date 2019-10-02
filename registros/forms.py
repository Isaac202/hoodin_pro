from django import forms
from registros.models import Registros


class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        #fields = ['codcliente', 'codservico', 'valor', 'data', 'caminho_arquivo', 'assinatura', 'versao',
         #         'descricao', 'codqrcode', 'codindicacao', 'desconto', 'resumo_obra']
        exclude = (

        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(RegistrosForm, self).__init__(*args, **kwargs)
        qs = Registros.objects.filter(codcliente=self.user)
        self.fields['codcliente'].queryset = qs




