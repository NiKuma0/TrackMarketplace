from .base import *


SECRET_KEY = 'django-insecure-g^9py14l%7i_^n7zy=v+gjio(ziy^ou6xqq70x0ggm%zh$t)w2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
