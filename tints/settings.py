from pathlib import Path
import os
import dotenv

dotenv.load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '80.78.246.133',
    '0.0.0.0',
    '127.0.0.1',
]

# Application definition
CORS_ORIGIN_ALLOW_ALL = True
INSTALLED_APPS = [
    'app',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tints.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'tints.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main',
        'USER': 'admin',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '80.78.246.133'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ON_SERVER = os.environ['PATH'].startswith('/usr')

STATIC_ROOT = '/var/static/tints/'  # ON_SERVER
# STATIC_ROOT = './static'  # on local
IMAGES_PATH = './static/img/'
STATIC_URL = '/static/'
PAYMENT_NOTIFICATION_PATH = 'order/paymentNotification'
# noinspection PyUnresolvedReferences
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"),
    ('img', './static/img')
    # './static/',
]

PAYMENT_TERMINAL_ID = os.environ.get("PAYMENT_TERMINAL_ID")
INIT_PAYMENT_URL = 'https://securepay.tinkoff.ru/v2/Init'

UNIONE_API_KEY = "695e163x51m969qm4unpwd8bx6jr7zoi1zp9cjfe"

SMS_LOGIN = "orightrussia"
SMS_PASSWORD = "oright2021"

HOST = "https://tintsofnature.ru"
