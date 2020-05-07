# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 16:44
# @Author  : punjen_yuan
# @File    : __init__.py.py


import os
from environs import Env

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # 静态回调, 引入APP
    @staticmethod
    def init_app(app):
        #  环境参数 默认为production
        ENV = env.str("FLASK_ENV", default="production")
        DEBUG = ENV == "development"
        PORT = env.int("PORT", default=5000)
        return


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or  'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

import redis
import logging


class Config(object):
    # DEBUG = True
    SECRET_KEY = 'kkajsnxwnnjs5586ded'
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:305634841@127.0.0.1:3306/flask_pujen?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = False
    # SQLAlchemy会记录所有发给stderr的语句,打印sql语句
    SQLALCHEMY_ECHO = True
    # 数据库连接池的大小
    SQLALCHEMY_POOL_SIZE = 5
    # 设定连接池的连接超时时间
    SQLALCHEMY_POOL_TIMEOUT = 15

    # flask_redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_URL = "redis://:305634841@localhost:6379/0"
    # flask_session的配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,password=305634841)
    SESSION_USE_SIGNER = True # 对cookies的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 # session数据有效期秒
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG
    # 设置邮件发送相关参数
    EMAIL_HOST = "smtp.163.com"
    EMAIL_USER = "13686821736@163.com"
    EMAIL_PORT= "25"
    # 邮箱授权码
    EMAIL_PASSWORD = "a305634841"
    EMAIL_SENDER = "13686821736@163.com"
    EMAIL_TITLE = "Interface Test Report"
    # 收件人
    EMAIL_RECEIVER = "305634841@qq.com/2870550420@qq.com/3067628559@qq.com"
    # 缓存设置
    CACHE_TYPE = "redis"
class DevelopConfig(Config):
    DEBUG = True
class productionConfig(Config):
    pass


config_map ={
    "develop": DevelopConfig,
    "online": productionConfig
}