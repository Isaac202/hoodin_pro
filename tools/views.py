from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.forms.models import ModelFormMetaclass
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from usuarios.models import UserConfirm
from usuarios.forms import UserCreationForm
from tools.genereteKey import generate_hash_key
# from tarefas_backgroud.tasks import send_mail
from tools.mail import send_mail_template


class MultiCreateView(CreateView):
    form_class = {}
    success_url = reverse_lazy('users:email_enviado')

    def dispatch(self, request, *args, **kwargs):
        if not type(self.form_class) is dict:
            raise ImproperlyConfigured(
                'form_class não é um dicionario, ex: form_class = {}')

        for form in self.form_class:
            if not isinstance(self.form_class[form], ModelFormMetaclass):
                msg = '{} não é uma instancia de ModelFom '.format(form)
                raise ImproperlyConfigured(msg)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        for form in self.form_class:
            kwargs[form] = self.form_class[form](
                self.request.POST or None, self.request.FILES or None)
        return kwargs

    def post(self, request, *args, **kwargs):
        for form in self.form_class:
            kwargs[form] = self.get_form(self.form_class[form])
            if kwargs[form].is_valid():
                continue
            else:
                return self.form_invalid(kwargs[form])

        return self.form_valid(**kwargs)

    def form_valid(self, **forms):
        # esse metodo deve ser implementado na class filho
        # os objetos teram que ser salvos manualmente na implementacao do metodo
        # e retornar self.get_success_url()
        msg = u'função form_valid não definida implemente a função na class filho, o retorno da função deve ser self.success_url()'
        raise NotImplementedError(msg)

    def get_success_url(self):
        # fazer alguma coisa antes e redireciona
        return HttpResponseRedirect(self.success_url)


class SignUpCreateView(MultiCreateView):

    form_class = None

    def dispatch(self, request, *args, **kwargs):
        self.set_form()
        return super().dispatch(request, *args, **kwargs)

    def set_form(self):
        # Obitenho o modelForm que contem o id_usuario e transformo form_class em um dicionario
        # E adiciono o UserCreationForm ao Formulario
        self.form_class = {'form': self.form_class,
                        #    'form_endereco': EnderecoMotoristaForm,
                           'form_user': UserCreationForm}

    def form_valid(self, **forms):
        context = {}
        person = forms['form'].save(commit=False)
        user= forms['form_user'].save()
        person.id_usuario = user
        person.save()
        forms['form'].save_m2m()
        context['site'] = settings.ALLOWED_HOSTS[0]
        context['nome'] = person.nome
        # person.token = userForm.getPassword()
        return self.login_redirect(user, context)

    def login_redirect(self, user, context):
        key = generate_hash_key(user.email)
        UserConfirm.objects.create(user=user, key=key)
        context['key'] = key
        send_mail_template(subject="Cadastro", template_name="usuarios/emailCadastro.html", context=context, recipient_list=[user.username])
        return self.get_success_url()


