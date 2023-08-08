from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

#region DEPLOYMENT SETTINGS
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']
#endregion DEPLOYMENT SETTINGS

SITE_ID = 1

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    #third party apps
    'taggit',
    'django.contrib.postgres',
    # custom apps
    'blog',

    'storages',
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

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'base.wsgi.application'

# DATABASES = {
#     'default': {

#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#     }
# }

DATABASES = {
    'default':dj_database_url.parse(os.environ.get('DATABASE_URL'))
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

#region TIME AND LANGUAGE
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True
#endregion TIME AND LANGUAGE

#region STATIC & MEDIA FILES + DEFAULT AUTO FIELD
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#endregion STATIC & MEDIA FILES + DEFAULT AUTO FIELD

#region EMAIL SETTINGS
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#endregion EMAIL SETTINGS

AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')

DEFAULT_FILE_STORAGE=os.environ.get('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE=os.environ.get('STATICFILES_STORAGE')

AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME