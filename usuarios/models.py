from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from tools.genereteKey import generate_hash_key


#from django.core.validators import validate_email
#from django.contrib.auth.validators import UnicodeUsernameValidator


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    #username_validator = UnicodeUsernameValidator()

    username = models.EmailField(
        _('email address'),
        # max_length=150,
        unique=True,
        #help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # validators=[username_validator],
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email confirmation'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.username)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def active(self):
        self.is_active = True
        super().save()

    def desactive(self):
        self.is_active = False
        super().save()


class User(AbstractUser):

    # indicacoes

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class UserConfirm(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usu??rio', on_delete=None
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{} em {}'.format(self.user, self.created_at)

    def conf(self):
        self.confirmed = True
        super().save()

    def status(self):
        return self.confirmed

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Usu??rio Confirmado'
        verbose_name_plural = 'Usu??rios Confirmados'



class Confuguracao(models.Model):
    dolar = models.DecimalField(max_digits=5, decimal_places=2, default=4)
    euro = models.DecimalField(max_digits=5, decimal_places=2, default=4)
    credito_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    valor_file = models.DecimalField(max_digits=5, decimal_places=2, default=0.50)
    atualiza????o = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)
    percentual = models.PositiveSmallIntegerField('percentual de pontua????o', default=10)
    pontuacao = models.DecimalField("Valor de resgate", max_digits=5, decimal_places=2, default=0.10)

    class Meta:
        verbose_name = _("Confugura??ao")
        verbose_name_plural = _("Confugura????es")

    def __str__(self):
        return "Configur????o"

    # def get_absolute_url(self):
    #     return reverse("Confuguracao_detail", kwargs={"pk": self.pk})
