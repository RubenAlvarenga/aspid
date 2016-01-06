from .base import *
import os

WKHTMLTOPDF_CMD='/usr/local/bin/wkhtmltopdf'
WKHTMLTOPDF_CMD_OPTIONS = {
   'quiet':True,
}

DEBUG = True
SESSION_COOKIE_AGE=1000

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aspid',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'aspid_test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aspid_test',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#AUTHENTICATION_BACKENDS = ('aspid.auth_backends.MyBackend',)



MEDIA_ROOT = BASE_DIR.child('media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/'#os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# #AUTH_PROFILE_MODULE = 'apps.autorizaciones.perfil'
MEDIA_URL = 'http://localhost:8000/media/'

