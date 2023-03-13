from django.utils.deconstruct import deconstructible
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


@deconstructible
class MobileNumberValidator(RegexValidator):
    regex = r'^(\+98|0)?9\d{9}$'
    message = _(
        "Phone number must be entered in the format: '09...' or format: '+989..."
    )
    flags = 0
