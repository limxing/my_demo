# -*- coding: utf-8 -*-

from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:leefeng@localhost:3306/leefeng?charset=utf8'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
