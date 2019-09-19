import os
from django.urls import reverse_lazy
from decouple import config
from dj_database_url import parse as dburl
from datetime import timedelta
from decimal import Decimal
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']


# Application definition

DEFAULT_APPS  = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'storages',
]

LIB_APPS = [
    'django_celery_results',
    'django_celery_beat',
    'rest_framework',
    'django_filters',
]

HOODID_APPS = [
    'arquivos',
    'bry',
    'serpro',
    'clientes',
    'configuracoes',
    'home',
    'indicacoes',
    'precos',
    'registros',
    'servicos',
    'usuarios',
    'tools',
    'extensoes',
]

INSTALLED_APPS = (
    DEFAULT_APPS + LIB_APPS + HOODID_APPS
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hoodid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hoodid.wsgi.application'
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db1.sqlite3')
DATABASES = {'default': config('DATABASE_URL', default=default_dburl,
                               cast=dburl), }
'''
#TODO ALTERA BASE ANTES DE COMMITA PRO REPOSITÓRIO

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hoodid',
        'USER': 'postgres',
        'PASSWORD': 'gmCz0OpsnkDpssyp',
        'HOST': '35.198.45.37',
        'PORT': '',
    }
}
'''



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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    'static'
]

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'


CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = config('REDIS_URL')
CELERY_BROKER_BACKEND = config('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vadejet.contato@gmail.com'
EMAIL_HOST_PASSWORD = 'linux162'
EMAIL_PORT = 587

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'hoodid_error.log',
        },
    },
    'loggers': {
        'tarefa_erro': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

ESTADOS_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

SEXO_CHOICES = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Outros', 'Outros'),
)

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'hoodidfile'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
AWS_LOCATION = 'static'
STATICFILES_DIRS = ['estaticos']

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATIC_ROOT = os.path.join(BASE_DIR, "static")


MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'
