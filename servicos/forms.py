from django import forms
from .models import Servicos, ServicosExtensoes # pega os campos e cria um form

class ServicosForm(forms.ModelForm):

    class Meta:
        model = Servicos
        #colocar os campos que não quer que apareça
        exclude = ['id']
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'


class BuscarForm(forms.Form):
    nome_servico = forms.CharField(label='nome', max_length=80, required=False)

class ServicosExtensoesForm(forms.ModelForm):

    nome_servico = forms.CharField(max_length=80, required=False)

    def _init_(self, user, *args, **kwargs):
        super(ServicosExtensoesForm, self)._init_(*args, **kwargs)
        #self.fields['codservico'].queryset = '1' #Servicos.objects.filter(id=user)
        self.fields['nome_servico'] = 'nome do servico' #Servicos.objects.filter(id=user)


class Meta:
        model = ServicosExtensoes
        #colocar os campos que não quer que apareça

        exclude = ['id']
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'


