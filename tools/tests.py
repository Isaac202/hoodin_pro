from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from motoristas.models import Motorista
from veiculos.models import Veiculo
from clientes.models import Cliente
from trajeto.models import Trajeto
from marca_veiculos.models import MarcaVeiculo
from modelo_veiculos.models import ModeloVeiuclo
from decimal import Decimal


class CustonTestCase(TestCase):
    # nome do model que esta sendo testando
    app_name = None

    def __init__(self, *args, **kwargs):
        if type(self.app_name) is str:
            return super().__init__(*args, **kwargs)
        raise ImproperlyConfigured(
            'app_name não definido, obs: variavel do tipo str deve conter o nome do app testado ')

    def create_user(self, username='teste@teste.com', password='qwerty123', login=False):
        # crio um usuario para o motorista
        self.user = get_user_model().objects.create_user(
            username, password)
        if login:
            # autenticio usuario criado no sistema
            self.client.force_login(self.user)
        return self.user

    def create_motorista(self, user=None):
        self.motorista = Motorista.objects.create(
            id_usuario=user or self.user, nome='fulano de tal',
            pai='joao', mae='maria', sexo='Masculino',
            data_nascimento="2000-12-02", cnh="001001001",
            fone_fixo="(99) 99999-9999", fone="(99) 99999-9999",
        )
        return self.motorista

    def create_cliente(self):
        self.passageiro = Cliente.objects.create(
            nome='fulano de tal',
            sexo='Masculino',
            data_nascimento="2000-12-02",
            cpf="001.001.001-65",
            fone="(99) 99999-9999",
            login_social="çekçlrkçel",
            email='aaa@a.com', senha='qwerty124'
        )

    def create_marca_modelo(self, marca="Ford", modelo="Mustang"):
        self.marca = MarcaVeiculo.objects.create(nome=marca)
        self.modelo = ModeloVeiuclo.objects.create(
            nome=modelo, marca=self.marca)

    def create_veiculo(self):
        self.veiculo = Veiculo.objects.create(
            id_motorista=self.motorista,
            placa='NXE3014', id_modelo=self.modelo,
            cor='azul', ano='2019',
            ano_modelo='2019', arcondicionado=True,
            internet=False
        )

    def create_corrida(self, valor_corrida=20.0, passageiro=None):
        self.corrida = Trajeto.objects.create(
            id_motorista=self.motorista,
            id_cliente=passageiro or self.passageiro,
            id_veiculo=self.veiculo,
            origem=128.00, destino=256.00,
            total_percurso=valor_corrida,
            status_trajeto="concluido",
            token='lfajsldfalff',
            valor=Decimal(str(valor_corrida)),
            ordem_trajeto=1,
        )

    def get_url(self, url, template=None, kwargs={}, data={}, status_code=200, expected_url=None, get_response=False):
        url = reverse_lazy(url, kwargs=kwargs)
        response = self.client.get(url, data)
        # html = response.content.decode('utf8')
        # self.assertIn('cadastro', html)
        if expected_url:
            self.assertEqual(response['location'], reverse_lazy(expected_url))
        self.assertEqual(response.status_code, status_code)
        if template:
            self.assertTemplateUsed(response, template)
        return self.getResultTest(response, get_response)

    def post_url(self, url, data, expected_url=None, template=None, status_code=302, get_response=False):
        url = reverse_lazy(url)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status_code)
        if expected_url:
            self.assertEqual(response['location'], reverse_lazy(expected_url))
        if template:
            self.assertTemplateUsed(response, template)

        return self.getResultTest(response, get_response)

    def post_url_form(self, url, data, expected_url=None, template=None, status_code=302, get_response=False):
        response = self.post_url(
            url, data, expected_url, template, status_code, True)
        # self.assertFormError(response, form, field, errors, msg_prefix)
        return self.getResultTest(response, get_response)

    def getResultTest(self, response, get_response):
        url = response.request['PATH_INFO']
        method = response.request['REQUEST_METHOD']
        if get_response:
            return response
        self.printTest(url, method)

    def printTest(self, url, method):
        if self.app_name is None:
            self.app_name = "Model não especificado:"
        print(self.app_name, ": "+method+": ", url)

    def getResponse(self, response, get_response=False):
        pass

    def reverse_lazy(self, url):
        return reverse_lazy(url)
