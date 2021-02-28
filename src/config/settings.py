import sys
from pathlib import Path

from .config import secret_key


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING
SECRET_KEY = secret_key



# This is our Base Dir of the project. (src)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# This is where our apps are situated.
APPS_ROOT = BASE_DIR / "apps"

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = BASE_DIR / 'staticfiles' / 'static'
STATIC_URL = "/static/"

# Media Files (User created IMG, doc....)
MEDIA_DIRS = BASE_DIR / 'media'
MEDIA_ROOT = BASE_DIR / 'staticfiles' / 'media'
MEDIA_URL = "/media/"



# Application definition
INSTALLED_APPS = [
    # --- Django Standart Apps ---
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --- User Created Apps ---
    'apps.core',
    # --- Additional Libs ---
    ]


ROOT_URLCONF = 'apps.core.urls'
WSGI_APPLICATION = 'config.wsgi.application'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware', # For translations
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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


AUTH_PASSWORD_VALIDATORS = [
    # Password validation
    # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Import Dev / Prod settings
if DEBUG:
    from .settings_dev import *
else:
    from .settings_prod import *
    STATIC_ROOT.mkdir(parents=True, exist_ok=True)
    MEDIA_ROOT.mkdir(parents=True, exist_ok=True)
