
from ..settings import DEBUG, INSTALLED_APPS, MIDDLEWARE, logger


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
    'django_cuser',
    'corpus',
    'chatstatement',
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


# Config for jalali_date App
CRISPY_TEMPLATE_PACK = 'crispy_forms'

# Persian Date Config for jalali_date App
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