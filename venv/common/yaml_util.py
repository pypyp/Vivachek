# coding=UTF-8
import os
import sys
import yaml
import csv
import path

sys.path.append(r'' + os.path.abspath('../'))


def read_csv():
    with open(r'' + path.get_project_path() + '\\data\\login.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            return row


def load(path):
    # open方法打开直接读出来
    f = open(path, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def read_url_csv():
    with open(r'' + path.get_project_path() + '\\data\\url.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            return row


def read_bastase_sql():
    with open(r'' + path.get_project_path() + '\\data\\database.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        return rows[1]


# 读取请求头
def read_yaml(key):
    with open(r'' + path.get_project_path() + '\\data\\basic_info\\headers\\extract.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


def read_mz_yaml():
    with open(os.getcwd() + '/mz_basic.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


def read_mz_blood_yaml():
    with open(os.getcwd() + '/mz_blood.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


def write_yaml(data, path):
    with open(path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def clear_yaml(path):
    with open(path, encoding='utf-8', mode='w') as f:
        f.truncate()
