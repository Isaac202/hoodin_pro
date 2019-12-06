from django.test import TestCase
from django.urls import reverse_lazy
from indicacoes.models import Indicacoes
from servicos.models import Servicos
from extensoes.models import Extensoes
from decimal import Decimal
# Create your tests here.


class SignupTest(TestCase):

    def setUp(self):
        self.indicacao = Indicacoes.objects.create(nome='TV')
        extensao = Extensoes.objects.create(nome='PDF')
        Servicos.objects.create(
            nome='This is a test',
            preco=Decimal('1.0'),
            tamanho=200,
        ).extensoes.add(extensao)
        Servicos.objects.create(
            nome='This is a test',
            preco=Decimal('1.0'),
            tamanho=200,
        ).extensoes.add(extensao)
        self.servicos = Servicos.objects.all()
        # print(self.servicos)

    def test_signup_basic(self):
        client = self.client
        url = reverse_lazy('cliente:new')
        client.post(url, data={
            
        })
