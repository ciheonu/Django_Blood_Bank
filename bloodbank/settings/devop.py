from . common import *
import os


SECRET_KEY = ''

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bloodbank',
        "HOST": 'localhost',
        "PORT": 3307,
        'USER': 'root',
        'PASSWORD': '',
    }
}
