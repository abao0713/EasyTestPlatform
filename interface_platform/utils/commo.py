# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 17:32
# @Author  : punjen_yuan
# @File    : commo.py
from interface_platform.models.table import InterfaceModel,InterfaceCase
# 格式
config = {"config":{
      "name": "testcase description",
      "variables": {
        "dd": 0
      },
      "parameters": {
        "ad": 0
      },
      "request": {
        "dd": 0
      },
      "setup_hooks": [
        "${hook_print(setup)}"
      ],
      "teardown_hooks": [
        "${hook_print(teardown)}"
      ]
    }}

class InterfaceConfig(object):
    """配置组装的基本类"""
    def __init__(self,req_pre_config):
        self.req_pre_config = req_pre_config.get("test_type")
    def config_name(self):
        if self.req_pre_config == 'run_project':
            "从请求体中拿出project"
            config_name = ''
        elif self.req_pre_config == 'run_suite':
            # 自定义明明
            config_name = 'run_suite'
        else:
            # 执行单个用例名称
            config_name = InterfaceModel.query(InterfaceModel.interface).filter_by(id=id).all()
        return config_name

    def config_variables(self):
        pass
    def config_parameters(self):
        pass
    def config_request(self):
        pass
    def config_setup_hooks(self):
        pass
    def config_teardown_hooks(self):
        pass
