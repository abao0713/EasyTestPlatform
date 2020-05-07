# --------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/2/15 20:26 
# @project_name : EasyTestPujen
# @author :	pujen_yuan
# ------------

from mainApp import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from interface_platform.models.table import *
from interface_platform.routes import app_user

app = create_app("develop")
app.register_blueprint(app_user, url_prefix='/user')
manager = Manager(app)
migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

"""终端运行1、 E:\Auto_test\EasyTestPujen>python3 manage.py db init
命令
2、 E:\Auto_test\EasyTestPujen>python3 manage.py db migrate --message "initial migration"
python3 manage.py db migrate --message "initial migration"
3、 E:\Auto_test\EasyTestPujen>python3 manage.py db upgrade

"""








