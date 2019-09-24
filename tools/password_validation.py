from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class ComplexPasswordValidator:
    """
    Validate whether the password contains minimum one uppercase, one digit and one symbol.
    """
    def validate(self, password, user=None):

        if re.search('[A-Z]', password)==None:
            raise ValidationError(
                _("Sua senha deve conter pelo menos um caractere maiúsculo."),
                code='password_is_weak',
            )
        if re.search('[0-9]', password)==None:
            raise ValidationError(
                _("Sua senha deve conter pelo menos UM número."),
                code='password_is_weak',
            )
        if re.search('[a-z]', password)==None:
            raise ValidationError(
                _("Sua senha deve conter pelo menos uma letra minúscula.."),
                code='password_is_weak',
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 number, 1 uppercase and 1 non-alphanumeric character.")