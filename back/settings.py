"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
load_dotenv()
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
  
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
		# "Elastic Beanstalk URL",
    "Pennypencebeans-env.eba-pemr7ys8.ap-northeast-2.elasticbeanstalk.com",
    "127.0.0.1",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    'accounts',
    'assets',
    'communities',
    'items',
    'auction',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # third party
    # django-rest-auth
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
  
    # django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_filters',
    
    # provider
    'allauth.socialaccount.providers.kakao',

    # CORS -> 프론트와 연결
    'corsheaders',

    # schedule
    'schedule',

    # 이미지 프로세서
    'imagekit',
    'sorl.thumbnail',

    # AWS 배포
    'storages',

    # API Swagger
    'rest_framework_swagger',
    'drf_yasg',

]

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

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]
CORS_ALLOW_CREDENTIALS = False

# CORS 관련 추가
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'access-control-request-method',
    'access-control-request-headers',
    'access-control-allow-origin',
    'content-type',
    'dnt',
    'pragma',
    'Expires',
    'origin',
    'cache-control',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-token',
    'Refresh',
)
ROOT_URLCONF = 'back.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = os.getenv('DATABASES')


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# kakao social login 
KAKAO_REST_API_KEY = os.getenv("KAKAO_REST_API_KEY")
SOCIAL_AUTH_KAKAO_SECRET = os.getenv("SOCIAL_AUTH_KAKAO_SECRET")


# rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATED_LOGOUT_REDIRECTS = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# User model
AUTH_USER_MODEL = "accounts.User"

# dj-rest-auth 설정
REST_USE_JWT = True

# django-allauth 설정
SITE_ID = 3
ACCOUNT_USER_MODEL_USERNAME_FIELD = None            # username 필드 사용 안함
ACCOUNT_EMAIL_REQUIRED = True                       # email 필드 사용 
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False                   # username 필드 사용 안함
ACCOUNT_AUTHENTICATION_METHOD = 'email'             # 이메일로 로그인
ACCOUNT_EMAIL_VERIFICATION = 'none'                 # 회원가입 시 이메일 인증 사용 안함

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),     # access 토큰 유효기간 테스트 할땐 짧게
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.CustomUserDetailsSerializer"
}  # 유저 회원가입

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "accounts.serializers.CustomUserDetailsSerializer",
} # SocialLoginView 사용때 만든 serializers.py로 변경

# 학교 알리미 API
ALIMI_API_KEY = os.getenv("ALIMI_API_KEY")

# 학교 검색을 위한 나이스 API
NEIS_API_KEY = os.getenv("NEIS_API_KEY")

# schedule 앱 설정
SCHEDULER_AUTOSTART = True
SCHEDULER_TIME_ZONE = 'Asia/Seoul'

# Media files (user uploaded filed)
MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'

        
# AWS 개발 & 배포 환경 분리
DEBUG = os.getenv("DEBUG") == "True"

if DEBUG == True: # 개발(로컬) 환경
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pennypence_DB',
        'USER': 'root',
        'PASSWORD': 'dlaudgkr12!',
        'HOST': 'localhost',
        'PORT': '3306',
        }
    }
    
else: # 배포(원격, 클라우드) 환경
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("DATABASE_NAME"), 
            "USER": "pennypence",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"), 
            "HOST": os.getenv("DATABASE_HOST"), 
            "PORT": "3306",
        }
    }

  
if DEBUG: 
    MEDIA_ROOT = BASE_DIR / 'images'
    MEDIA_URL = '/media/'

else:   
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )

# 상단에 다시 작성함.  
# if DEBUG == True: # 개발(로컬) 환경
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': BASE_DIR / 'db.mysql',
#         }
#     }

# else: # 배포(원격, 클라우드) 환경
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": os.getenv("DATABASE_NAME"),
#             "USER": "pennypence",
#             "PASSWORD": os.getenv("DATABASE_PASSWORD"), # .env 파일에 value 작성
#             "HOST": os.getenv("DATABASE_HOST"), # .env 파일에 value 작성
#             "PORT": "3306",
#         }
#     }