import os

from .base import *


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'HOST': os.getenv('HOST') or 'db',
            'USER': os.getenv('USER'),
            'DBNAME': os.getenv('DBNAME'),
            'PORT': os.getenv('PORT') or 5432,
        }
    }
}
