from django import forms
from .models import Servicos, ServicosExtensoes # pega os campos e cria um form

class ServicosForm(forms.ModelForm):

    class Meta:
        model = Servicos
        #colocar os campos que não quer que apareça
        exclude = (
            #'token', 'status', 'pontuacao', 'data_cadastro',
            #'id_usuario', 'valor_atual_credito', 'role','email','senha','confirma_sms',
            #'status_motorista', 'status_veiculos' #'foto_perfil'
        )

class BuscarForm(forms.Form):
    nome_servico = forms.CharField(label='nome', max_length=80, required=False)

class ServicosExtensoesForms(forms.ModelForm):
    class Meta:
        model = ServicosExtensoes
'''
    def __init__(self, user,  *args, **kwargs):
          super(ServicosExtensoesForms, self).__init__(*args, **kwargs)
          #self.fields['id_placer'].queryset = Placer.objects.filter(perfil=user)

        fields = ['id_placer', 'tipo', 'nome', 'descricao', 'nome_area',
                  'media', 'area2', 'area3', 'area4', 'ativo']

        exclude = ['id', 'id_campanha', 'data_cadastro', 'url_placer', 'url_anunciante',
                   'qtd_visitas', 'qtd_cliques', 'tempo_visualizacao', ]
'''

class BuscarExtensoesForm(forms.Form):
    nome_extensao = forms.CharField(max_length=10, required=True)
