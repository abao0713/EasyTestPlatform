# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 16:49
# @Author  : punjen_yuan
# @File    : table.py

from interface_platform.extensions import db




models = db.column
class InterfaceModel(db.Model):
    """接口信息表"""
    __tablename__ = "interface_info"
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(35), unique=True, nullable=False, comment="接口所属模块")
    interface = db.Column(db.String(35), nullable=False, unique=True, comment="接口名称")
    preInterface = db.Column(db.String(35), nullable=False, comment="前置接口名称id")
    method = db.Column(db.String(35), nullable=False, comment="请求方式")
    Description = db.Column(db.String(35), nullable=False, comment="接口描述")
    host = db.Column(db.String(35), nullable=False, comment="接口host地址")
    url = db.Column(db.String(35), nullable=False, comment="接口api地址")
    value = db.Column(db.String(35), nullable=False, comment="默认请求参数")
    service = db.Column(db.String(35), nullable=False, comment="接口所属于的服务")
    mock_interface = db.Column(db.String(35), nullable=False, comment="mock接口地址")
    field_info = db.Column(db.String(35), nullable=False, comment="接口请求字段限制")
    marks = db.Column(db.String(35), nullable=False, comment="备注")
    create_time = db.Column(db.String(35), nullable=False)
    update_time = db.Column(db.String(35), nullable=False)


    class Meta:
        unique_together = (("id", "interface_platform"),)
        db_table = "interface_info"
        verbose_name = '接口表'
        verbose_name_plural = verbose_name

class InterfaceCase(db.Model):
    """接口信息表"""
    __tablename__ = "interface_case_info"
    id = db.Column(db.Integer, primary_key=True)
    case_name = db.Column(db.String(35), unique=True, nullable=False, comment="用例名称")
    params = db.Column(db.String(35), nullable=False, unique=True, comment="请求参数")
    expect_result = db.Column(db.String(35), nullable=False, comment="期望结果")
    create_time = db.Column(db.String(35), nullable=False, comment="创建时间")
    update_time = db.Column(db.String(35), nullable=False, comment="更新时间")
    interface_name_id = db.Column(db.String(35), nullable=False, comment="对应接口id")
    level = db.Column(db.String(35), nullable=False, comment="用例等级")
    setUp = db.Column(db.String(35), nullable=False, comment="用例前置处理")
    tearDown = db.Column(db.String(35), nullable=False, comment="用例后置处理")
    remarks = db.Column(db.String(35), nullable=False, comment="用例备注")
    status = db.Column(db.String(35), nullable=False, comment="用例激活状态")
    environment = db.Column(db.String(35), nullable=False, comment="用例运行环境")
    preInterface = db.Column(db.String(35), nullable=False, comment="前置接口")
    mock_id = db.Column(db.String(35), nullable=False, comment="用例mock_id")


