from django import forms
from registros_coautores.models import Coautores

class CoautoresForm(forms.ModelForm):
    
    class Meta:
        model = Coautores
        exclude = ("arquivo",)
