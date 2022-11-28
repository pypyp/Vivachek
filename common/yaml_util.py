# coding=UTF-8
import os
import sys
import yaml
import csv
from path import get_project_path

sys.path.append(r'' + os.path.abspath('../'))


def load(path):
    # open方法打开直接读出来
    f = open(path, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    return data


# 读取请求配置信息
def read_yaml(key):
    with open(r'' + get_project_path() + '\\data\\basic_info\\headers\\extract.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入
def write_yaml(data, path):
    with open(path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清除配置信息
def clear_yaml(path):
    with open(path, encoding='utf-8', mode='w') as f:
        f.truncate()
