from django.test import TestCase
from decouple import config
from .tasks import  comprar_credito
from cielo.tasks import gerar_token_cartao
from cielo.tasks import comprar_com_token
from cielo.tasks import criar_token_senha
from cielo.tasks import cancelar_compra


class TestCielo(TestCase):
    def test_merchant_id(self):
        mid = config('MERCHANT_ID')
        assert mid=='4dfff8d6-4e18-4d7d-af75-8c9345b0c5cb'

    def test_merchant_key(self):
        mid = config('MERCHANT_KEY')
        assert mid=='K8nfYeNg1CtSyKN8DO4SfSyx37Wq0JAyUpFF2phL'

    def test_merchant_id_box(self):
            mid = config('MERCHANT_ID_BOX')
            assert mid=='bde2dd94-207b-4303-8939-11f18389a67f'

    def test_merchant_key_box(self):
            mid = config('MERCHANT_KEY_BOX')
            assert mid=='SGZZBNYUQFFBCCXABXJRDSSEDCPAWBYXCZGYQSMF'

    def test_url_token_sms(self):
            mid = config('URL_TOKEN_SMS')
            assert mid=='https://api.directcallsoft.com/request_token'

    def test_sms_url(self):
        url_sms = config('SMS_URL_ENVIO')
        assert url_sms=='https://api.directcallsoft.com/sms/send'


    def test_url_producao_post(self):
                url = config('CIELO_PRD_PUT_POST')
                assert url=='https://api.cieloecommerce.cielo.com.br/'


    def test_url_producao_get(self):
                url = config('CIELO_PRD_GET')
                assert url=='https://apiquery.cieloecommerce.cielo.com.br/'


    def test_compra_autorizada(self):
        resposta_cielo, trasacao, codigo = comprar_credito(10, 'Martoele C. Pixão', '0662821825086128', '279',
                                                   'HiperCardCLS', '07/2022', 200, 1)

        assert resposta_cielo == 'Autorizacao negada'


    '''
    def test_cacelar_compra(self):
        resultado = cancelar_compra('19536d55-5305-468b-86d9-3432bba0d414', 200 )

        assert resultado !=None
    '''
    #TODO Realizar teste com cartao de verdade amanha

