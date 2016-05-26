# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014/2015

Django settings for runner project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ROOT_PROJECT = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(ROOT_PROJECT)

DIRNAME = os.path.dirname(__file__)

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

SITE_ID = 1
#print("settings for site id %s"%SITE_ID)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9a3!-fum*4g2f5&zyqoj0&9vk*ahqmk12yfu9nymsr(6+^$#ma'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = [
    "127.0.0.1", 
    "localhost", 
    'runner.nerim.net', 
    'pahpa'
]
SERVE_MEDIA = DEBUG
DBMUGU = True

# Application definition
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
#from django.conf.global_settings import STATICFILES_FINDERS as SF

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'account.context_processors.account',
    'pinax_theme_bootstrap.context_processors.theme',
)

DEFAULT_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    'django.contrib.humanize',
  
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'django_forms_bootstrap',
    'bootstrapform',
    'account',
 
 
)

#TODO: auto_loader a faire sur RUNNER_APPS
RUNNER_APPS = (
    'runner',
    'blacklist', 
    'pinax_theme_bootstrap',

)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + RUNNER_APPS


DOCS_ROOT = os.path.join(PROJECT_PATH, 'docs/_build/html')
DOCS_ACCESS = 'staff'
SPHINXDOC_BUILD_DIR = os.path.join(PROJECT_PATH, 'docs/_build')

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
#    'easy_thumbnails.processors.colorspace',
#    'easy_thumbnails.processors.autocrop',
#    #'easy_thumbnails.processors.scale_and_crop',
#    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
#    'easy_thumbnails.processors.filters',

#    'runner.middleware.runner_tz.TimezoneMiddleware', 
)

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = (
#    '178.132.17.172',
#    )
#CORS_URLS_REGEX = r'^/api/.*$'


AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'guardian.backends.ObjectPermissionBackend',
    'runner.backends.auth_backends.RunnerUserModelBackend', 
)
#ANONYMOUS_USER_ID = -1 #guardian conf

ACCOUNT_USE_AUTH_AUTHENTICATE = True
ACCOUNT_EMAIL_UNIQUE = False
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_OPEN_SIGNUP = False
THEME_ACCOUNT_ADMIN_URL = True
THEME_CONTACT_EMAIL = 'runner@nerim.com'
#LOGIN_URL='/account/login/'
#LOGOUT_URL='/account/logout/'
ROOT_URLCONF = 'runner.urls'

WSGI_APPLICATION = 'runner.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        #'rest_framework.renderers.XMLRenderer',
        # 'rest_framework.renderers.YAMLRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend', ),
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata', 
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'PAGINATE_BY': 10,
    'HYPERLINKED': True,  # Retourne les relations sous forme de liens ou de grappes d'objets
}


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




#DATABASE_ROUTERS = ['runner.router.DatabaseAppsRouter']
#DATABASE_APPS_MAPPING = {'runner': 'runner'}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'

USE_I18N = True
USE_L10N = True
#USE_TZ = True
USE_TZ = False

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# WARNING: Mettre en place la gestion staticfile si django non serveur de media static
#                   http://localhost/static par exemple
MEDIA_ROOT = ''

MEDIA_URL = "/media/"
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/runner/static/'

#STATICFILES_DIRS = (
#    'static',
#)

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
#    '/var/www/pahpa/',
)

SUIT_CONFIG = {
    'HEADER_DATE_FORMAT': 'l, j/m/Y',

    'MENU': (
        'sites',
        {'app': 'auth', 'permissions': 'auth.add_user','models': ('user', 'group')},
        '-',
        {'label': 'Runner', 'icon':'icon-cog', 'url': '/'},
        {'app':'dashboard', 'label':'Dashboard', 'models':
            ('dashboard', 'injectorstate', 'todo')
        }, 
        {'app': 'customers', 'label': 'Reseller/Client','models':
            ('reseller',
            'client'
            )},
        {'app': 'lines', 'label': 'Operator','models':
            ('telcoinjector', 
            'telco', 
            'telcoparsingwords', 
            'telcoparsing'
            )},  
        'voice',
        {'app': 'valo', 'label': 'Price Purchasing','models': 
            (
            'juridiction_purchase',
            'juridiction',
            'ga_telco',
            'ga_juridiction', 
            )},
        {'app': 'valo', 'label': 'Price Reselling','models': 
            (
#            'juridiction_selling',
            'gv_telco',
            'gv_telcodetail', 
            'gv_indicatifdetail', 
            'gv_clientdetail',
            'gv_sipaccountdetail',
#            'gv_svadetail',
#            'gv_ndi',
            )},
        
        {'label': 'Valo', 'permissions' : 'valo.add_cdr','models': ('valo.cdr', 'valo.resellerscdr', 'valo.revcdr')},
        
#        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
#            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
#        ]},
        
        {'app': 'ie', 'label': 'Import Export'},
        '-', 
        '-', 
        {'label': 'Test Login', 'icon':'icon-question-sign', 'url': '/accounts/login/'},
        {'label': 'Test Logout', 'icon':'icon-question-sign', 'url': '/accounts/logout/'},
        '-', 
        {'label': 'Helpdesk', 'icon':'icon-question-sign', 'url': '/helpdesk/'},
        '-', 
        'mugu', 
    )
}
FILEBROWSER_SUIT_TEMPLATE = True 

CRISPY_TEMPLATE_PACK = 'foundation-5'

#DJANGO_COLORS="error=yellow/blue,blink;notice=magenta"

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': False,
    'form_error_class': 'bootstrap3-error',
    'form_required_class': 'bootstrap3-required',
    'javascript_in_head': True,
    'jquery_url': '/static/runner/jquery/js/jquery-2.1.1.min.js',
    'base_url': '/static/runner/bootstrap/'
}


