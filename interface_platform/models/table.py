# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 16:49
# @Author  : punjen_yuan
# @File    : table.py

import json
from datetime import datetime
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, VARCHAR
from mainApp.database import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy
# 初始化数据库连接:
engine = sqlalchemy.create_engine("mysql+pymysql://testgroup:123456@10.201.5.161:3306/platform",encoding="utf-8", pool_size=5, pool_pre_ping=True)
# 创建ORM连接
Base = declarative_base(engine)

class InterfaceModel(db.Model):
    '''
    接口模块
    '''
    interface = models.CharField(max_length=255, unique=True, default='',  verbose_name='接口名称')
    type = models.IntegerField(null=False, default=0,verbose_name='类型')
    preInterface = models.CharField(max_length=255, null=False,default='', verbose_name="前置接口")
    method = models.CharField(max_length=20, choices=request_methods, verbose_name="请求方法")
    Description = models.CharField(max_length=255, null=True, verbose_name="接口描述")
    URL = models.CharField(max_length=255, null=True, verbose_name="接口地址")
    value = models.CharField(max_length=500, null=True, verbose_name='接口默认测试数据')
    service = models.CharField(max_length=255,default='', verbose_name='服务方')
    field_info = models.CharField(max_length=500, default='', verbose_name='接口字段信息')
    marks = models.TextField(default='', verbose_name='备注信息')
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")



    class Meta:
        unique_together = (("id", "interface_platform"),)
        db_table = "t_interface_info"
        verbose_name = '接口表'
        verbose_name_plural = verbose_name



Base.metadata.create_all(engine)

# 创建事务
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
