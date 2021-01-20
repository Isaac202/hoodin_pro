from django import forms
from .models import Avaliadores
from pycpfcnpj import cpfcnpj

class CreateAvaliadoresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateAvaliadoresForm, self).__init__(*args, **kwargs)
        # self.fields['saldo'].widget.attrs['readonly'] = True




    class Meta:
        model = Avaliadores
        fields = ['nome', 'cnpj']
        exclude = ['id','data_cadastro']

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get("cnpj")
        masked_cnpj_number = cpfcnpj.clear_punctuation(cnpj)

        if cpfcnpj.validate(masked_cnpj_number)==False:
              raise forms.ValidationError("Cnpj Inválido")

        return cnpj


class BuscaAvaliadoresForm(forms.Form):
    busca = forms.CharField(label='Avaliadores', max_length=80, required=False)

