# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 16:44
# @Author  : punjen_yuan
# @File    : __init__.py.py


import os
import redis as redis
from environs import Env
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    # flask_redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_URL = "redis://:305634841@localhost:6379/0"
    # flask_session的配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=305634841)
    SESSION_USE_SIGNER = True  # 对cookies的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据有效期秒
    # 日志配置 ###############################################################
    LOG_PATH = os.path.join(basedir, "logs", "falling-wind-service.log")
    LOG_FORMATTER = (
        "%(asctime)s [%(name)s] [%(thread)d:%(threadName)s] "
        "%(filename)s:%(module)s:%(funcName)s "
        "in %(lineno)d] "
        "[%(levelname)s]: %(message)s"
    )
    LOG_MAX_BYTES = 50 * 1024 * 1024  # 日志文件大小
    LOG_BACKUP_COUNT = 10  # 备份文件数量
    LOG_INTERVAL = 1
    LOG_WHEN = "D"

    # 设置邮件发送相关参数
    EMAIL_HOST = "smtp.163.com"
    EMAIL_USER = env.str("EMAIL_PASSWORD", default="13686821736@163.com")
    EMAIL_PORT = "25"
    # 邮箱授权码
    EMAIL_PASSWORD = env.str("EMAIL_SENDER", default="a305634841")
    EMAIL_SENDER = env.str("EMAIL_PASSWORD", default="13686821736@163.com")
    EMAIL_TITLE = "Interface Test Report"
    # 收件人
    EMAIL_RECEIVER = "305634841@qq.com,2870550420@qq.com"
    # 缓存设置
    CACHE_TYPE = "redis"
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
    MAIL_USE_TLS = True
    SQLALCHEMY_DATABASE_URI = env.str('DEV_DATABASE_URL',default="mysql+pymysql://root:305634841@127.0.0.1/flasken?charset=utf8")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env.str('DEV_DATABASE_URL',default="mysql+pymysql://root:305634841@127.0.0.1/flasken?charset=utf8")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


