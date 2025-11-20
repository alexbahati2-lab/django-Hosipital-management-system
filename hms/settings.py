import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*i5k978@le&vfxejb3fyc#h@!-!a9=6%og8pk8$uiwz6qq8re$'

# DEBUG MUST BE FALSE ON RENDER
DEBUG = False

# Allow Render domains
ALLOWED_HOSTS = ["hms-9ovy.onrender.com", "localhost", "127.0.0.1"]



# Application definition

INSTALLED_APPS = [
    "jazzmin",  
    'accounts',
    'reception',
    'doctor',
    'pharmacy',
    'lab',
    'billing',
    'nursing',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ⭐ REQUIRED for Render static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hms.urls'

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

WSGI_APPLICATION = 'hms.wsgi.application'


# Database — keep SQLite for now
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------- STATIC FILES FOR RENDER ----------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"   # ⭐ Render needs this folder
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []

# Whitenoise settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'


# Jazzmin configuration
JAZZMIN_SETTINGS = {
    "site_title": "HMS Admin",
    "site_header": "Hospital Management System 🏥",
    "site_brand": "HMS Dashboard",
    "welcome_sign": "Welcome to Hospital Management System",
    "copyright": "© 2025 Sholix HealthTech",
    "theme": "flatly",
    "show_ui_builder": False,
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"app": "reception"},
        {"app": "pharmacy"},
        {"app": "lab"},
        {"app": "doctor"},
        {"app": "nursing"},
        {"app": "billing"},
    ],
}
