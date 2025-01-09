from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-78%&12-82mv1e34e*2!6y6!+e)rmjmbhu-%y6^gu0(f38!l3k*"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# rocketman/settings/dev.py






try:
    from .local import * 
except ImportError:
    pass
