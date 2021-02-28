from .settings import BASE_DIR
from .config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DOMAINS



# Whom can have acces to this site.
ALLOWED_HOSTS = ['localhost', DOMAINS]





# DataBase
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        }
    }
