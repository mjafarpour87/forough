from .settings import *
import os
from django.utils.translation import gettext_lazy as _

import logging
# Get an instance of a logger
logger = logging.getLogger('settings')
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

INSTALLED_APPS += [
    'crispy_forms',
    'rosetta',  
    'jalali_date',
    # 'django_select2',
    'chatterbot.ext.django_chatterbot',
]

MIDDLEWARE += [
    'django.middleware.locale.LocaleMiddleware', # For multilingual
]


# My apps
INSTALLED_APPS += [
    'users',
    'organization',
    'corpus',
]




if DEBUG:
    # Django Debug Toolbar 
    logger.debug("Django Debug Toolbar configuration done.")
    INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]
    INSTALLED_APPS += [
    'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware', # Django Debug Toolbar 
    ]

# Update TEMPLATES by ref
template_path_list = []
template_path_list = TEMPLATES[0]['DIRS']
template_path_list.append(BASE_DIR / 'templates')
template_path_list.append(BASE_DIR / 'users' / 'templates' )
template_path_list.append(BASE_DIR / 'organization' / 'templates'  )
template_path_list.append(BASE_DIR / 'corpus' / 'templates'  )



CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization

LANGUAGES = (
    ('en', _('English')),
    ('fa', _('Persian')),
)

LOCALE_PATHS = [
        BASE_DIR / 'locale', 
]

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# User Authentication config
LOGIN_URL = '/users/accounts/login'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "dashboard"
AUTH_USER_MODEL = "users.CustomUser"  


# Logging Config
LOGGING = {
        'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },

    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}


# Persian Date Config
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}


# # Django’s cache framework
# # https://docs.djangoproject.com/en/4.1/topics/cache/
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
#     ,'select2': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# # Tell select2 which cache configuration to use:
# SELECT2_CACHE_BACKEND = "select2"


#Email settings details 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = '172.18.244.140' 
EMAIL_USE_TLS = False 
EMAIL_PORT = 2525 
EMAIL_HOST_USER = 'no-reply@django.iums.com' 
EMAIL_HOST_PASSWORD = '************' 

# Chatterbot Django Settings
CHATTERBOT = {
    'name': 'Tech Support Bot',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
}


logger.debug(f"------------------DEBUG = {DEBUG}" )
logger.debug(f"BASE_DIR         : {BASE_DIR}")
logger.debug(f"LOCALE_PATHS     : {LOCALE_PATHS}")
if DEBUG:
    logger.debug(f"STATICFILES_DIRS : {STATICFILES_DIRS}")
else:
    logger.debug(f"STATIC_ROOT      : {STATIC_ROOT}")
logger.debug(f"STATIC_URL       : {STATIC_URL}")
logger.debug(f"MEDIA_URL        : {MEDIA_URL}")
logger.debug(f"MEDIA_ROOT       : {MEDIA_ROOT}")
# logger.debug(template_path_list)