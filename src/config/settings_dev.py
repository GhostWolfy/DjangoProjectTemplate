"""
Django settings.
For more information https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from .settings import BASE_DIR



# Whom can have acces to this site.
ALLOWED_HOSTS = ['localhost', '127.0.0.1']



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
