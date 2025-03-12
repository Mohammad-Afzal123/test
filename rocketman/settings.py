import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (User uploads, images, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CSRF_TRUSTED_ORIGINS = [
    "https://suganyaramamoorthy.com",
    "https://www.suganyaramamoorthy.com"
]
ALLOWED_HOSTS = [
    "64.227.150.192",
    "suganyaramamoorthy.com",
    "www.suganyaramamoorthy.com"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newdb',
        'USER': 'newuser',
        'PASSWORD': 'newpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
