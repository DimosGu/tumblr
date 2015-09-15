import os

# SESSION_COOKIE_DOMAIN = '.briansquashic.com'
SESSION_COOKIE_DOMAIN = '.local.n-ws.org'
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'inpr6-d-pan0@gtsj%at1gy!=ds+xms@y2s%q&$-4q(k_s4b6e'

DEBUG = True

ALLOWED_HOSTS = ['.briansquashic.com', '.local.n-ws.org']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.no_user',
    'apps.user_accounts',
    'apps.dashboard',
    'apps.blog',
    'apps.explore',
    'apps.sites',
    'apps.search',
    'apps.following',
    'apps.likes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'tumblr.subdomain_middleware.SubdomainMiddleware',
)

ROOT_URLCONF = 'tumblr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR +'/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.core.context_processors.media',
                'tumblr.custom_context.blog',
                'tumblr.custom_context.header_forms',
                'tumblr.custom_context.site',
                'tumblr.custom_context.domain_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'tumblr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'user_accounts.User'

LOGIN_URL = '/login'