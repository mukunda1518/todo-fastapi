import os

SECRET_KEY = os.environ.get("SECRET_KEY", '')
TOKEN_LIFETIME = os.environ.get("TOKEN_LIFETIME", 1)