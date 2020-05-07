# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 19:38
# @Author  : punjen_yuan
# @File    : extensions.py

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail_import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
