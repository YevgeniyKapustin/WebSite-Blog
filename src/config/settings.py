"""Django settings for blog project."""
import os
from pathlib import Path

from typing import Any, List
from pydantic_settings import BaseSettings


class DjangoSettings(BaseSettings):
    """Manage all the project settings"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DATABASES: dict = self.__get_databases()

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SECRET_KEY: str
    DEBUG: bool

    ALLOWED_HOSTS: List[str] = ['*']

    LANGUAGE_CODE: str = 'ru'
    TIME_ZONE: str = 'Europe/Moscow'
    USE_I18N: bool = True
    USE_TZ: bool = True

    INSTALLED_APPS: list[str] = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'articles',
        'about',
        'mailing',
    ]

    MIDDLEWARE: list[str] = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF: str = 'config.urls'

    TEMPLATES: list[dict] = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION: str = 'config.wsgi.application'

    DEFAULT_ENGINE: str
    DEFAULT_NAME: str
    DEFAULT_USER: str
    DEFAULT_PASSWORD: str
    DEFAULT_HOST: str
    DEFAULT_PORT: str
    DATABASES: dict = {'default': None}

    AUTH_PASSWORD_VALIDATORS: list[dict] = [
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

    STATIC_URL: str = 'static/'
    STATIC_ROOT: str = os.path.join(BASE_DIR, 'src')
    STATICFILES_DIRS: list = [os.path.join(BASE_DIR, 'static')]

    MEDIA_URL: str = 'media/'
    MEDIA_ROOT: str = os.path.join(BASE_DIR, 'media')

    DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

    def __get_databases(self) -> dict:
        return {
            'default': {
                'ENGINE': self.DEFAULT_ENGINE,
                'NAME': self.DEFAULT_NAME,
                'USER': self.DEFAULT_USER,
                'PASSWORD': self.DEFAULT_PASSWORD,
                'HOST': self.DEFAULT_HOST,
                'PORT': self.DEFAULT_PORT
            }
        }

    class Config:
        env_file: str = '../.env'
        env_file_encoding: str = 'utf-8'


_settings: dict = DjangoSettings().dict()


def __dir__() -> List[str]:
    """The list of available options from DjangoSettings object."""
    return list(_settings.keys())


def __getattr__(name: str) -> Any:
    """Turn the module access into a DjangoSettings access."""
    return _settings[name]
