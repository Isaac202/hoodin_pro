from cielo.tasks import comprar_credito
from django import forms
from random import randint
from .models import Compras 
from datetime import date

class InserirCreditoForm(forms.Form):

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

    nome_cartao = forms.CharField(max_length=60, required=True)
    numero_cartao = forms.CharField(max_length=30, required=True)
    seguranca = forms.CharField(max_length=3, required=True)
    bandeira = forms.ChoiceField(required=True, choices=BANDEIRA_CHOICES)
    validade = forms.CharField(max_length=7, required=True, label="Validade: MM/YYYY")
    valor = forms.DecimalField(
        max_digits=10, decimal_places=2, required=True, localize=True)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        for field in self.fields:
            if field == 'validade':
                self.fields[field].widget.attrs['placeholder'] = 'Ex: 12/{}'.format(today.year)
            self.fields[field].widget.attrs['class'] ='form-control'
     

    def clean(self):
      try:

        nome_cartao = self.cleaned_data.get("nome_cartao")
        numero_cartao = self.cleaned_data.get("numero_cartao")
        seguranca = self.cleaned_data.get("seguranca")
        bandeira = self.cleaned_data.get("bandeira")
        validade = self.cleaned_data.get("validade")
        valor = self.cleaned_data.get("valor")
        qtd = 1#self.cleaned_data.get('qtd_parcela')
        val = valor *100
        val = int(val)
        pedido = randint(1,1000000)
        data = comprar_credito(pedido, nome_cartao,numero_cartao, seguranca, bandeira, validade, val, qtd)
        resposta_cielo, codigo_tran = data
        # print(data,'\n\n')
        # self.cleaned_data.__setitem__("codigo_trasacao", codigo_tran)
        # self.cleaned_data.__setitem__("statu_trasacao", resposta_cielo)

      except Exception as e:
          print(e)


