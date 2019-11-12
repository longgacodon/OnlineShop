import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_^ay*q02t#vh&!kac0t^ebm5b84_)#+h6wczspen88g21lv!j_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['elecream.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'crispy_forms',
    'home.apps.HomeConfig',
    'order.apps.OrderConfig',
    'product.apps.ProductConfig',
    'cart.apps.CartConfig',
    'coupon.apps.CouponConfig',
    'django.contrib.postgres',
#    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'localhost',
        'PORT': '8000',
        'USER': 'postgres',
        'PASSWORD': '1',
    }
}

#Authentication
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'home.authentication.EmailAuthBackend',
#    'social_core.backends.google.GoogleOAuth2',
]

#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1024428038184-ip8bfhuo64jmthhgpb5k8b4u4ah23gpr.apps.googleusercontent.com' # Google Consumer Key
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'UQgk9i3P-69NVGORpXL_wGIW' # Google Consumer Secret

CART_SESSION_ID = 'cart'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Thoundsand Seperator
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR='.'
NUMBER_GROUPING=3

#URL
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Static files (CSS, JavaScript, Images)
    #Static
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'home/static'),
)
    #Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')