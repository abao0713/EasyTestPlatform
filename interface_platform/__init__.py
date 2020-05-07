# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 16:44
# @Author  : punjen_yuan
# @File    : __init__.py.py
from flask import Flask
from config import config
from interface_platform.extensions import bootstrap, db, moment, ckeditor, mail, loginManager
import os

def create_app(config_name = None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask('interface_platform', static_folder="../static",static_url_path='/static/',template_folder='../templates')
    app.config.from_object(config[config_name])

    register_logging(app)  # 注册日志处理器
    register_extensions(app)  # 注册扩展（扩展初始化）
    register_blueprints(app)  # 注册蓝本
    register_commands(app)  # 注册自定义shell命令
    register_errors(app)  # 注册错误处理函数
    register_shell_context(app)  # 注册错误处理函数
    register_template_context(app)  # 注册模板上下文处理函数
    return app

def register_logging(app):
    pass  #后续介绍日志
# 工厂模式
def flask_log(config_name):
    """

    :param config_name: 传入日志等级
    :return:
    """
    # 设置日志的的等级
    logging.basicConfig(level=config_map[config_name].LOG_LEVEL)
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100,backupCount=100)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().addHandler(file_log_handler)

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

def register_blueprints(app):
    app.register_blueprint(auth, url_prefix = '/auth')

def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db = db)

def register_template_context(app):
    pass

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

def register_commands(app):
    pass