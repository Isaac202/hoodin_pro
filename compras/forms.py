from cielo.tasks import comprar_credito
from django import forms
from random import randint
from .models import Compras


class InserirCreditoForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):

        super(InserirCreditoForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.fields['codigo_trasacao'].widget.attrs['readonly'] = True
        self.fields['statu_trasacao'].widget.attrs['readonly'] = True
        self.fields['statu_trasacao'].widget = forms.HiddenInput()
        self.fields['qtd_parcela'].widget.attrs['readonly'] = True

    BANDEIRA_CHOICES = (
        ('Visa', 'Visa'),
        ('Master', 'Master'),
        ('Hipercard', 'Hipercard'),
        ('Hiper', 'Hiper'),
        ('American Express', 'American Express'),
        ('Elo', 'Elo'),
        ('Diners Club', 'Diners Club'),
        ('American Express', 'American Express'),
        ('Discover', 'Discover'),
        ('JCB', 'JCB'),
        ('Aura', 'Aura'),

    )




    nome_cartao = forms.CharField(max_length=60, required=False)
    numero_cartao = forms.CharField(max_length=30, required=False)
    seguranca = forms.CharField(max_length=3, required=False)
    bandeira = forms.ChoiceField(required=False, choices=BANDEIRA_CHOICES)
    validade = forms.CharField(max_length=7, required=False)
    valor = forms.DecimalField(max_digits=10, decimal_places=2, required=True, localize=True)



    class Meta:
        model = Compras
        fields = ['valor', 'forma_pagamento', 'nome_cartao','numero_cartao', 'seguranca', 'bandeira',
                  'validade', 'valor', 'qtd_parcela', 'codigo_trasacao', 'statu_trasacao']
        exclude = ['id','data_compra']

    def clean(self):
      try:

        nome_cartao = self.cleaned_data.get("nome_cartao")
        numero_cartao = self.cleaned_data.get("numero_cartao")
        seguranca = self.cleaned_data.get("seguranca")
        bandeira = self.cleaned_data.get("bandeira")
        validade = self.cleaned_data.get("validade")
        valor = self.cleaned_data.get("valor")
        qtd = self.cleaned_data.get('qtd_parcela')
        val = valor *100
        val = int(val)
        pedido = randint(1,1000000)
        resposta_cielo, codigo_tran = comprar_credito(pedido, nome_cartao,numero_cartao, seguranca, bandeira, validade, val, qtd)

        self.cleaned_data.__setitem__("codigo_trasacao", codigo_tran)
        self.cleaned_data.__setitem__("statu_trasacao", resposta_cielo)

      except Exception as e:
          print(e)


