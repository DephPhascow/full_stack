from pathlib import Path
import constants
BASE_DIR = Path(__file__).resolve().parent.parent
import os


SECRET_KEY = constants.SECRET

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', constants.SITE_HOST]


INSTALLED_APPS = [
    'adminactions',
    'django_admin_index',
    'ordered_model',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    'strawberry_django',
    "tinymce",
    "import_export",
    'debug_toolbar',
    'simple_history',
    'corsheaders',
    # 'strawberry_django_jwt.refresh_token',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",   
    'simple_history.middleware.HistoryRequestMiddleware',
    'strawberry_django.middlewares.debug_toolbar.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # 'strawberry_django_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ['http://localhost:8080']

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "back.wsgi.application"

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': constants.DB_NAME,
        'USER': constants.DB_LOGIN,
        'PASSWORD': constants.DB_PASSWORD,
        'HOST': constants.DB_HOST,
        'PORT': constants.DB_PORT
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = "media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale/"), )
SIMPLE_HISTORY_REVERT_DISABLED = False

STRAWBERRY_DJANGO = {
    "FIELD_DESCRIPTION_FROM_HELP_TEXT": True,
    "TYPE_DESCRIPTION_FROM_MODEL_DOCSTRING": True,
    "MUTATIONS_DEFAULT_ARGUMENT_NAME": "input",
    "MUTATIONS_DEFAULT_HANDLE_ERRORS": True,
    "GENERATE_ENUMS_FROM_CHOICES": False,
    "MAP_AUTO_ID_AS_GLOBAL_ID": True,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'