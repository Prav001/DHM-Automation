"""
Django settings for automation project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from __future__ import unicode_literals

import os
import sys

gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


    
DEBUG = True
TEMPLATE_DEBUG = DEBUG

##ADMINS = (
##    ('Praveen', 'praveensharma900@gmail.com'),
##)
##
##MANAGERS = ADMINS

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz' ,
    'django.contrib.messages.context_processors.messages',
   
)

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

AUTHENTICATION_BACKENDS = (
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail  
)

##APP_PATH = os.path.dirname(os.path.abspath(__file__))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ko4lu-#c@kj5v(1=ks7h66-de*i7clc4r#h_#x=j@w#oe*=z09'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID=2

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'automation.urls'


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django_admin_bootstrapped',
    'django_admin_bootstrapped.bootstrap3',
    'admin_tools', 
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django_tables2',
    'crispy_forms',
    'registration',
    'home',
    'consistency',
    'filters',
    'masters',
    'transactions',
    'suit',
    'bootstrap3',
    'bootstrap_toolkit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'sqlserver_ado.sql_app',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'datetimewidget',
    'ajax_select',
    'django_windows_tools',
    'django.contrib.sitemaps',
    'django.contrib.admindocs',
    'chosen',
    'viewform',
    'django_pandas',
    #'highcharts',
    # 'jquery',
    #'chartit'
        


)

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_OPEN = 'TRUE'
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Registration]'
LOGIN_REDIRECT_URL = '/'   
LOGIN_URL = '/accounts/login/'




MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
  
)
PASSWORD_HASHERS = (
 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
 'django.contrib.auth.hashers.BCryptPasswordHasher',
 'django.contrib.auth.hashers.SHA1PasswordHasher',
 'django.contrib.auth.hashers.MD5PasswordHasher',
 'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
 'django.contrib.auth.hashers.CryptPasswordHasher')


WSGI_APPLICATION = 'automation.wsgi.application'



# Django Suit configuration example
SUIT_CONFIG = {
     #header
     
     'ADMIN_NAME': 'Praveen',
     'HEADER_DATE_FORMAT': 'l, j. F Y',
     'HEADER_TIME_FORMAT': 'H:i',

     #forms
      'SHOW_REQUIRED_ASTERISK': True,  # Default True
      'CONFIRM_UNSAVED_CHANGES': True, # Default True

     #menu
      'SEARCH_URL': '/admin/auth/user/',
      'MENU_ICONS': {
         'sites': 'icon-leaf',
         'auth': 'icon-lock',
      },
      'MENU_OPEN_FIRST_CHILD': True, # Default True
      #'MENU_EXCLUDE': ('auth.group',),
      'MENU': (
          'sites',
          {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
          {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
          {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
      ),

      #misc
      'LIST_PER_PAGE': 15
}



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'sqlserver_ado',
    'NAME': 'testing',
    'USER': 'sa',
    'PASSWORD': 'development12$',
    'HOST': 'RAMCOBL267',
    'PORT': '',
}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


USE_I18N = True

USE_L10N = False

USE_TZ = True

LANGUAGE_CODE = 'en-us'

gettext_noop = lambda s: s

# here is all the languages supported by the CMS
PAGE_LANGUAGES = (
    ('de', gettext_noop('German')),
    ('fr-ch', gettext_noop('Swiss french')),
    ('en-us', gettext_noop('US English')),
)

# copy PAGE_LANGUAGES
languages = list(PAGE_LANGUAGES)

# redefine the LANGUAGES setting in order to be sure to have the correct request.LANGUAGE_CODE
LANGUAGES = languages

TIME_ZONE = 'Asia/Calcutta'
DATE_FORMAT = 'Y N j'
DATE_INPUT_FORMATS =(
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = "/static/admin/"

# STATICFILES_DIRS = (
#    "C:/Python34/Scripts/automation/",
#  )
#  STATIC_ROOT = "C:/Python34/Scripts/automation/static"

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SEND_ACTIVATION_EMAIL = True
EMAIL_USE_TLS = True 
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER= 'praveensharma900@gmail.com'
EMAIL_HOST_PASSWORD= 'Mulder321'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass





# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': False,
    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
    'javascript_in_head': True,
}

