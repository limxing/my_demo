# -*- coding: utf-8 -*-

import os

from flask import Config
from flask_uploads import IMAGES

class BaseConfig(Config):
    APP = "socketdemo"
    APP_NAME_CN = "socketdemo"
    SECRET_KEY = "65US7Cc8AF8dd4"
    BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = False
    TESTING = False
    UPLOADED_PHOTO_DEST = os.path.join(BASEDIR,'upload')
    UPLOADED_PHOTO_ALLOW = IMAGES

