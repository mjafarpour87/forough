"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-70n+()o0^7cmlrz_4hy=qir3p1c(oq_2jl@g)zz7@wl81sm=k)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forough.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n', # for translation
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'forough.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



LANGUAGES = (
    ('en', _('English')),
    ('fa', _('Persian')),
)

LOCALE_PATHS = [
        os.path.join(BASE_DIR, "locale"), 
]





STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Extend Setting 
from .settingsextended.logging_setting import *
from .settingsextended.app_middleware_setting import *
from .settingsextended.template_setting import *
from .settingsextended.authentication_setting import *
from .settingsextended.file_setting import *
from .settingsextended.cache_setting import *
from .settingsextended.email_setting import *

# print last setting and configuration
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

# Chatterbot Django Settings
CHATTERBOT = {
    'name': 'Tech Support Bot',
    'logic_adapters': [
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
}