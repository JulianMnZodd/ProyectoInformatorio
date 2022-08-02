from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5qy)gvc!(edu!2&m2bio2466lt+88rx44$)5$##l4ts##w4+)i'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}