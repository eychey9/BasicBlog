from distutils.debug import DEBUG
import django_on_heroku
from decouple import config
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['dolcerellando.herokuapp.com']

