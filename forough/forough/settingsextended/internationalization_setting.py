from django.utils.translation import gettext_lazy as _
from ..settings import BASE_DIR


# Internationalization
LANGUAGES = (
    ('en', _('English')),
    ('fa', _('Persian')),
)

LOCALE_PATHS = [
        BASE_DIR / 'locale', 
]