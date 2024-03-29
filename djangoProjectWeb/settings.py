"""
Django settings for djangoProjectWeb project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+2yfb5lpfo7&a9ubxe3voi+kpdi!a^r$muc5h$)e=*8tju8od*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',  # Antes de 'django.contrib.admin'
    'camaraComercio',
    'nested_admin',
    'comentarios',
    'Cursos',
    'estados',
    'emprendimiento',
    'inventario',
    'ckeditor',
    'users',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'storages',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',  # o la skin que prefieras
        'toolbar': 'Full',  # Puedes personalizar la barra de herramientas como prefieras
        'height': 200,
        'width': 'auto',
        'extraPlugins': 'widget',  # Si necesitas widgets
        # ... Más configuraciones según tus necesidades ...
    },
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]
CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'djangoProjectWeb.urls'
import os # necesario para el siguiente código

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# JET CUSTOM 111827
JET_DEFAULT_THEME = 'light-green'  # O cualquier otro tema disponible
JET_SIDE_MENU_COMPACT = True  # Para un menú lateral más compacto
JET_CHANGE_FORM_SIBLING_LINKS = True  # Para mostrar los botones de "Guardar y continuar editando" y "Guardar y agregar otro" en la parte superior del formulario
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
DEBUG = True
X_FRAME_OPTIONS = 'SAMEORIGIN'



WSGI_APPLICATION = 'djangoProjectWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pruebisima2',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # O la dirección del servidor de tu base de datos
        'PORT': '3306',        # El puerto de MySQL, por defecto es 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

REST_FRAMEWORK = {
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
   ],
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework.authentication.TokenAuthentication',
   )
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTH_USER_MODEL = 'users.User'
