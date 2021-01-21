from django import forms
from .models import Instituicoes_Arquivos
# from .models import Anuncio
from instituicoes.models import Instituicoes
from avaliadores.models import Avaliadores
from decimal import Decimal
from django.conf import settings
from datetime import datetime
from cloudinary.forms import CloudinaryFileField
from django.forms.widgets import HiddenInput


class CreateInstituicoes_ArquivosForm(forms.ModelForm):
    novo_valor = forms.DecimalField(max_digits=14, decimal_places=2, initial=0)

    class Meta:
        model = Instituicoes_Arquivos
        fields = ['id_avaliador', 'nome', 'data_inicial', 'data_final', 'valor', 'ativa']
        exclude = ['id', 'data_cadastro']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateInstituicoes_ArquivosForm, self).__init__(*args, **kwargs)
        qs = Avaliadores.objects.filter(perfil=self.user)
        self.fields['id_avaliador'].queryset = qs

        if self.instance.pk is None:
            self.fields['novo_valor'].widget.attrs['readonly'] = True

        else:
            self.fields['novo_valor'].widget.attrs['readonly'] = False
            self.fields['valor_campanha'].widget.attrs['readonly'] = True

    def clean_valor_campanha(self):

        nome_anun = self.cleaned_data.get("id_avaliador")
        avaliador = Avaliadores.objects.filter(id=nome_anun.id)
        codigo = 0
        val_avaliador = 0
        valcampanha_banco = str(self.cleaned_data.get("valor_campanha"))
        valcampanha_banco = valcampanha_banco.replace(",", ".")

        valcamp = Decimal(valcampanha_banco)
        val_atual = 0

        for an in avaliador:
            val_anunciante = Decimal(an.saldo)
            codigo = an.id

        if val_anunciante < valcamp:
            raise forms.ValidationError(
                "a valor da campanha maior que o Saldo do Anunciante, Saldo: " + str(val_anunciante))


        else:
            val_anunciante = val_anunciante - valcamp
            if self.instance.pk is None:
                atualizar_saldo = Avaliadores.objects.filter(id=codigo).update(saldo=val_anunciante)

        return valcamp

    def clean_novo_valor(self):
        if self.instance.pk is not None:
            vcamp = self.cleaned_data.get("valor_campanha")
            if vcamp == None or '':
                vcamp = 0

            vnovo = self.cleaned_data.get("novo_valor")
            if vnovo == None or '':
                vnovo = 0

            nome_anun = self.cleaned_data.get("id_avaliador")
            avaliador = Avaliadores.objects.filter(id=nome_anun.id).first()
            codigo_avaliador = nome_anun.id
            val_avaliador = avaliador.saldo
            valcamp = Decimal(vcamp)
            val_novo = Decimal(vnovo)
            valor_atual = 0

            if val_novo > 0:
                if val_avaliador < val_novo:
                    raise forms.ValidationError(
                        "a valor da campanha maior que o Saldo do Anunciante, Saldo: " + str(val_avaliador))
                else:
                    val_avaliador = val_avaliador - val_novo
                    valcamp = valcamp + val_novo
                    self.cleaned_data['valor_campanha'] = valcamp

            else:
                valor_atual = valcamp + val_novo
                if valor_atual < 0:
                    raise forms.ValidationError(
                        "a valor da campanha nao pode ser menor q zero: " + str(valor_atual))
                else:
                    self.cleaned_data['valor_campanha'] = valor_atual
                    val_avaliador = val_avaliador - val_novo

            atualizar_saldo = Avaliadores.objects.filter(id=codigo_avaliador).update(saldo=val_avaliador)
            return val_novo

    def clean_data_final(self):
        data_ini = self.cleaned_data.get("data_inicial")
        data_fim = self.cleaned_data.get("data_final")

        if data_ini > data_fim:
            raise forms.ValidationError("Data inicial maior que data final")
        return data_fim

    def clean_data_inicial(self):
        data_ini = self.cleaned_data.get("data_inicial")
        data_atual = datetime.today().date()

        if self.instance.pk is None:
            if data_ini < data_atual:
                raise forms.ValidationError("Data inicial não pode ser menor que data do dia")

        return data_ini

#    def clean_id_avaliador(self):

#        settings.CODIGO_ANUNCIANTE = self.cleaned_data.get("id_anunciante")
#        codigo = self.cleaned_data.get("id_anunciante")

#        return codigo


class BuscaInstituicoes_ArquivosForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)


class BuscaResumoForm(forms.Form):
    OP_CHOICES = (
        ('Ativas', 'Ativas'),
        ('Encerradas', 'Encerradas'),
        ('Todas', 'Todas'),
    )

    nome = forms.ChoiceField(required=False, choices=OP_CHOICES)
    nome_camp = forms.CharField(max_length=100, required=False)
#    place = forms.ModelChoiceField(queryset=Placer.objects.all())


# class InserirAnuncioForms(forms.ModelForm):
#    AREA_CHOICES = (
#        ('Area1', 'Area1'),
#        ('Area2', 'Area2'),
#        ('Area3', 'Area3'),
#        ('Area4', 'Area4'),
#    )

#    nome_area = forms.ChoiceField(required=True, choices=AREA_CHOICES,
#                                  widget=forms.Select(attrs={'onchange': "exibir_ocultar();"}))

#    media = CloudinaryFileField(
#        options={'folder': 'area1/',
#                 },
#        required=False
#    )
#    area2 = CloudinaryFileField(
#        options={'folder': 'area2/'},
#        required=False
#    )
#    area3 = CloudinaryFileField(
#        options={'folder': 'area3/'},
#        required=False
#    )
 #   area4 = CloudinaryFileField(
 #       options={'folder': 'area4/'},
 #       required=False
 #   )

 #   def __init__(self, user, *args, **kwargs):
 #       super(InserirAnuncioForms, self).__init__(*args, **kwargs)

 #   class Meta:
 #       model = Anuncio

 #       fields = ['id_placer', 'tipo', 'nome', 'descricao', 'nome_area',
 #                 'media', 'area2', 'area3', 'area4', 'ativo']

 #       exclude = ['id', 'id_campanha', 'data_cadastro', 'url_placer', 'url_anunciante',
 #                  'qtd_visitas', 'qtd_cliques', 'tempo_visualizacao', ]


# class BuscaAnuncioForm(forms.Form):
#    nome = forms.CharField(max_length=100, required=True)
