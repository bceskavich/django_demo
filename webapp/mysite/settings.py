"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zb0$ctmfq$_z5ksi9t0^*ws&d)%ovwaocmdxbi%w1)i^3qv7fo'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),   
)

########              LOAD SETTINGS FROM ENV VARS              ########
#our helper function that makes it easy to get env vars or raise an error

def get_env_variable(var_name, required=True, is_int=False, is_boolean=False, default=None):

    """ Get the environment variable or return exception """
    try:
        env_var = os.environ[var_name]
        if is_int:
            try:
                return int(env_var)
            except ValueError:
                error_msg = "%s environment variable must be a number" % var_name
                raise ImproperlyConfigured(error_msg)
        elif is_boolean:
            if env_var == "TRUE":
                return True
            else:
                return False
        else:
            return env_var
    except KeyError:
        if required:
            error_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(error_msg)
        else:
            return default

#DATABASES

#TODO non-default database
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


DEBUG = get_env_variable('DEBUG', required=False, is_boolean=True, default=True)
TEMPLATE_DEBUG = DEBUG
CSRF_COOKIE_SESSION = get_env_variable('CSRF_COOKIE_SESSION', required=False, is_boolean=True, default=False)
SESSION_COOKIE_SECURE = get_env_variable('SESSION_COOKIE_SECURE', required=False, is_boolean=True, default=False)
ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS', required=False).split(',')  \
    if get_env_variable('ALLOWED_HOSTS', required=False) else []
STATIC_URL = get_env_variable('STATIC_URL', required=False, default='/')

#DATABASE

DATABASES['default']['ENGINE'] = get_env_variable(
    'DATABASE_DEFAULT_ENGINE', required=False, default='django.db.backends.sqlite3')
DATABASES['default']['NAME'] = get_env_variable(
    'DATABASE_DEFAULT_NAME', required=False, default=path(ROOT, 'db.sqlite3'))
DATABASES['default']['USER'] = get_env_variable('DATABASE_DEFAULT_USER', required=False, default='')
DATABASES['default']['PASSWORD'] = get_env_variable('DATABASE_DEFAULT_PASSWORD', required=False, default='')
DATABASES['default']['HOST'] = get_env_variable('DATABASE_DEFAULT_HOST', required=False, default='')
DATABASES['default']['PORT'] = get_env_variable('DATABASE_DEFAULT_PORT', required=False, is_int=True, default='')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
