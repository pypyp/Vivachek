# coding=UTF-8
from common.yaml_util import clear_yaml
from config.contast import Path

"""
    每次运行清空基础配置信息
"""
def clear():
    for i in Path.path['basic'].values():
        clear_yaml(i)