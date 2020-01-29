from django import forms
from registros_coautores.models import Coautores

class CoautoresForm(forms.ModelForm):
    
    class Meta:
        model = Coautores
        exclude = ("arquivo",)
        
    def clean_percentual_obra(self):
        data = self.cleaned_data["percentual_obra"]
        if data > 0:
            return data
        raise forms.ValidationError('Porcentagem deve ser maior que zero')
    
