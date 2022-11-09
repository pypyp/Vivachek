# coding=UTF-8
import os
import sys
import time
from common.yaml_util import write_yaml, read_yaml
from common.read_yaml import load
from config.contast import Url, Path
from common.httpClient import RequestMain
import random

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_qc_info():
    qc_data = {"pageNo": 1, 'pageSize': 15}

    value = 15.3
    liquid = random.choice(load(Path.path['basic']['LIQUID_INFO']))
    paper = random.choice(load(Path.path['basic']['PAPER_INFO']))

    if read_yaml('headers')["Platform"] == '3':
        sn = random.choice(load(Path.path['basic']['SN_INFO']))

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

    qc_add_data = {
        "value": value,
        "sn": sn,
        "liquidId": liquid['id'],
        'paperId': paper['id'],
        "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "result": result,
    }

    if read_yaml('headers')["Platform"] == '1':
        qc_data['sn'] = read_yaml('headers')["sn"]
        qc_add_data["sn"] = read_yaml('headers')["sn"]
    response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
                               json={"pageNo": 1, 'pageSize': 15})
    if response['data']['count'] == 0:
        re.request_main('post', Url.QC_ADD, headers=read_yaml('headers'),
                        json=qc_add_data)
    response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
                               json=qc_data)
    write_yaml(response['data']['lists'][0], Path.path['basic']['QC_INFO'])


get_qc_info()