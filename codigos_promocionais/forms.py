from django import forms
from .models import Codigos_Promocionais#, ServicosExtensoes # pega os campos e cria um form

class Codigos_PromocionaisForm(forms.ModelForm):

    class Meta:
        model = Codigos_Promocionais
        #colocar os campos que não quer que apareça
        exclude = ['id']


class BuscarForm(forms.Form):
    promocao = forms.CharField(label='nome', max_length=80, required=False)

