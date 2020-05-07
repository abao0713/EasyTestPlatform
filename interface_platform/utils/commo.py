# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 17:32
# @Author  : punjen_yuan
# @File    : commo.py

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
    def __init__(self,req_pre_config):
        self.req_pre_config = req_pre_config.get("test_type")
        pass
    def config_name(self):
        if self.req_pre_config == 'run_project'
            pass
        elif self.req_pre_config == 'run_suite'
            pass
        else:
            # 运行单个用例
            pass
