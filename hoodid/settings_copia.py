import os
from django.urls import reverse_lazy
from decouple import config
from dj_database_url import parse as dburl
from datetime import timedelta
from decimal import Decimal
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = True # config('DEBUG', default=False, cast=bool)aa

ALLOWED_HOSTS = ['registrosonline.com.br','localhost', '127.0.0.1', '*']

DEFAULT_APPS = [
    'admin_menu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


LIB_APPS = [
    'django_celery_results',
    'django_celery_beat',
    'rest_framework',
    'django_filters',
    'multiselectfield',
    'rangefilter',
    'django_countries'
    # 'daterangefilter',
    # 'import_export',

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
    'area_atuacao',
    'compras',
    'clientes_atuacao',
    'cielo',
    'servicos_extensoes',
    'tarefas_backgroud',
    'codigos_promocionais',
    'registros_coautores',
    'instituicoes',
    'instituicoes_arquivos',
    'avaliadores'
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

#35.198.56.23 10.158.0.5pytpp
DEV = config('DEV', default=False, cast=bool)
if DEV:
    default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'hdb2.sqlite3')
    DATABASES = {'default': config('DATABASE_URL', default=default_dburl,
                               cast=dburl), }
else:

    SESSION_COOKIE_AGE = 30*60
    SESSION_SAVE_EVERY_REQUEST = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'banco_hoodid',
        'USER': 'postgres',
        'PASSWORD': 'gmCz0OpsnkDpssyp',
        'HOST': '35.198.45.37',
        'PORT': '',
       }
    }



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

AUTH_USER_MODEL = 'usuarios.User'
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/



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
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
DEFAULT_EMAIL = "hoodidregistrosonline@gmail.com;contato@hoodid.com"
# EMAIL_USE_TLS = True




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
    ('AP', 'Amap??'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Cear??'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Esp??rito Santo'),
    ('GO', 'Goi??s'),
    ('MA', 'Maranh??o'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Par??'),
    ('PB', 'Para??ba'),
    ('PR', 'Paran??'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piau??'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rond??nia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'S??o Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

DISTRITOS_PORTUGAL_CHOICES = (
    ('Aveiro', 'Aveiro'),
    ('Beja', 'Beja'),
    ('Braga', 'Braga'),
    ('Bragan??a', 'Bragan??a'),
    ('Castelo Branco', 'Castelo Branco'),
    ('Coimbra', 'Coimbra'),
    ('Evora', 'Evora'),
    ('Faro', 'Faro'),
    ('Guarda', 'Guarda'),
    ('Leiria', 'Leiria'),
    ('Lisboa', 'Lisboa'),
    ('Portalegre', 'Portalegre'),
    ('Porto', 'Porto'),
    ('Santarem', 'Santarem'),
    ('Setubal', 'Setubal'),
    ('Viana do Castelo', 'Viana do Castelo'),
    ('Vila Real', 'Vila Real'),
    ('Viseu', 'Viseu')
)

DISTRITOS_ESPANHA_CHOICES = (
    ('Alava', 'Alava'),
    ('Albacete', 'Albacete'),
    ('Alicante', 'Alicante'),
    ('Almer??a', 'Almer??a'),
    ('Asturias', 'Asturias'),
    ('Avila', 'Avila'),
    ('Badajoz', 'Badajoz'),
    ('Barcelona', 'Barcelona'),
    ('Burgos', 'Burgos'),
    ('Caceres', 'Caceres'),
    ('Cadiz', 'Cadiz'),
    ('Cantabria', 'Cantabria'),
    ('Castellon', 'Castellon'),
    ('Ciudad Real', 'Ciudad Real'),
    ('Cordoba', 'Cordoba'),
    ('La Coru??a', 'La Coru??a'),
    ('Cuenca', 'Cuenca'),
    ('Gerona', 'Gerona'),
    ('Granada', 'Granada'),
    ('Guadalajara', 'Guadalajara'),
    ('Guipuzcoa', 'Guipuzcoa'),
    ('Huelva', 'Huelva'),
    ('Huesca', 'Huesca'),
    ('Baleares', 'Baleares'),
    ('Jaen', 'Jaen'),
    ('Leon', 'Leon'),
    ('Lerida', 'Lerida'),
    ('Lugo', 'Lugo'),
    ('Madrid', 'Madrid'),
    ('Malaga', 'Malaga'),
    ('Murcia', 'Murcia'),
    ('Navarra', 'Navarra'),
    ('Orense', 'Orense'),
    ('Palencia', 'Palencia'),
    ('Las Palmas', 'Las Palmas'),
    ('Pontevedra', 'Pontevedra'),
    ('La Rioja', 'La Rioja'),
    ('Salamanca', 'Salamanca'),
    ('Segovia', 'Segovia'),
    ('Sevilla', 'Sevilla'),
    ('Soria', 'Soria'),
    ('Tarragona', 'Tarragona'),
    ('Santa Cruz de Tenerife', 'Santa Cruz de Tenerife'),
    ('Teruel', 'Teruel'),
    ('Toledo', 'Toledo'),
    ('Valencia', 'Valencia'),
    ('Valladolid', 'Valladolid'),
    ('Vizcaya', 'Vizcaya'),
    ('Zamora', 'Zamora'),
    ('Zaragoza', 'Zaragoza')
)


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
)


TIPOPESSOA_CHOICES = (
    ('J', 'Juridica'),
    ('F', 'Fisica'),
)

ESTADO_CIVIL_CHOICES = (
    ('C', 'Casado'),
    ('S', 'Solteiro'),
    ('D', 'Divorciado'),
    ('V', 'Viuvo'),

)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "estaticos")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# STORAGE DE CONFIGRUCAO DO AWS
#----------------------------------------------------------------------------
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_LOAD_METADATA = False
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
    AWS_DEFAULT_ACL = "private"
    AWS_BUCKET_ACL = "private"


    #Static assets
    #---------------------------------------------------------------------------
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
    STATIC_URL = f'///s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    # uplaod dos arqivos
    #--------------------------------------------------------------------------

    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
    MEDIA_URL = f'///s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'
    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'estaticos')
# ]

ADMIN_LOGO = 'imgs/logo-hoodid.png'


ADMIN_STYLE = {
    'background': 'white',
    'primary-color': '#205280',
    'primary-text': '#d6d5d2',
    'secondary-color': '#3B75AD',
    'secondary-text': 'white',
    'tertiary-color': '#F2F9FC',
    'tertiary-text': 'black',
    'breadcrumb-color': 'whitesmoke',
    'breadcrumb-text': 'black',
    'focus-color': '#eaeaea',
    'focus-text': '#666',
    'primary-button': '#26904A',
    'primary-button-text':' white',
    'secondary-button': '#999',
    'secondary-button-text': 'white',
    'link-color': '#333',
    'link-color-hover': 'lighten($link-color, 20%)',
    'logo-width': '165px',
    'logo-height': '53px'
    #3308
    #1064
}

LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('users:redirect')

# IMPORT_EXPORT_USE_TRANSACTIONS = True

SIMPLE_EMAIL_CONFIRMATION_AUTO_ADD = True
EMAIL_CONFIRMATION_PERIOD_DAYS = 7
SIMPLE_EMAIL_CONFIRMATION_PERIOD = timedelta(days=EMAIL_CONFIRMATION_PERIOD_DAYS)

DOLAR_VALOR = 4
EURO_VALOR = 4
VALOR_CREIDITO_INCIAL = Decimal('1.00')


