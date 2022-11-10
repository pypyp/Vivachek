# coding=UTF-8
import os
import sys
import time
from testCase.log import logger
from common.yaml_util import  read_yaml, load
import random
from config.contast import Url, Path
from common.httpClient import RequestMain

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def qc_data():
    value = 15.3
    liquid = random.choice(load(Path.path['basic']['LIQUID_INFO']))
    paper = random.choice(load(Path.path['basic']['PAPER_INFO']))
    if read_yaml('headers')["Platform"] == '1':
        sn = read_yaml('headers')["sn"]

    else:
        sn = random.choice(load(Path.path['basic']['SN_INFO']))['sn']

    if liquid['type'] == 0:
        if value < paper['lowMinLimit'] or value > paper['lowMaxLimit']:
            result = 1
        else:
            result = 0

    elif liquid['type'] == 1:
        if value < paper['mediumMinLimit'] or value > paper['mediumMaxLimit']:
            result = 1
        else:
            result = 0
    else:
        if value < paper['mediumMinLimit'] or value > paper['mediumMaxLimit']:
            result = 1
        else:
            result = 0
    data = {
        "value": value,
        "sn": sn,
        "liquidId": liquid['id'],
        'paperId': paper['id'],
        "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "result": result,
    }
    return data


def qc_add():
    data = qc_data()
    logger.log_info.info("添加质控数据")
    response = re.request_main('post', Url.QC_ADD, headers=read_yaml('headers'),
                               json=data)
    if response["code"] == 0:
        logger.log_info.info("质控添加成功")
        return True
