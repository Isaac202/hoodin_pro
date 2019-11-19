from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
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



from django.core.mail import EmailMessage

def send_mail():
    email = EmailMessage(
        'Hello',
        'Email funcionando',
        'hoodidregistrosonline@gmail.com',
        # 'myconsult.orders@gmail.com',
        ['jf.interatividade@gmail.com',],#,'volneyrock@gmail.com'],
        reply_to=['another@example.com'],
        headers={'Message-ID': 'foo'},
    )
    try:
        email.send()
        print("email enviado")
    except:
        print('deu merda')