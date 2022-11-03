# coding=UTF-8
import os
import sys
import yaml

sys.path.append(r'' + os.path.abspath('../'))


def load(path):
    # open方法打开直接读出来
    f = open(path, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    return data

