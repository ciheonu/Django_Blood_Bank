from . common import *
import os


SECRET_KEY = 'django-insecure-f5o&x^ytrslci1+uz%m5#jtm9#s=@(#lhg&6)h9wd_tx5#^1tv'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bloodbank',
        "HOST": 'localhost',
        "PORT": 3307,
        'USER': 'root',
        'PASSWORD': 'Webro123$',
    }
}