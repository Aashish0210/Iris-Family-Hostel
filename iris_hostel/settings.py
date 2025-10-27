from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# Security & Debug
# --------------------
SECRET_KEY = 'dev-secret-key-change-me'  # Replace with a secure key for production
DEBUG = False
ALLOWED_HOSTS = ['AashishPradhan.pythonanywhere.com']  # Your live domain

# --------------------
# Media
# --------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------
# Email defaults
# --------------------
DEFAULT_FROM_EMAIL = 'no-reply@yourdomain.com'
ADMIN_EMAIL = 'admin@yourdomain.com'

# --------------------
# Installed apps
# --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'kids',
    'billing',
    'widget_tweaks',
]

# --------------------
# Middleware
# --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------
# URLs & Templates
# --------------------
ROOT_URLCONF = 'iris_hostel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Project-level templates
        'APP_DIRS': True,  # App-level templates
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

WSGI_APPLICATION = 'iris_hostel.wsgi.application'
ASGI_APPLICATION = 'iris_hostel.asgi.application'

# --------------------
# Database
# --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------
# Auth validators
# --------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------
# Internationalization
# --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_TZ = True

# --------------------
# Static files
# --------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Optional global static folder
STATIC_ROOT = BASE_DIR / 'staticfiles'   # For collectstatic

# --------------------
# Default primary key
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------
# Authentication redirects
# --------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
