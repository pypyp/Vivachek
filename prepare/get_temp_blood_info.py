# coding=UTF-8
import os
import sys
import time
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.httpClient import RequestMain
from datetime import datetime

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_temp_blood_info():
    glu_data ={
        "startTime": datetime.now().strftime('%Y-%m-%d 00:00:00'),
        "endTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    }

    add_data = {
        "value": 6.2,
        "valueUnit": 1,
        "method": 0,
        "nurseId": read_yaml('userId'),
        "timeType": "q2h",
        "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "unusual": 1
    }

    if read_yaml('headers')["Platform"] == '1':
        glu_data ={}
        add_data["method"] = 1
        add_data['deviceNo'] = read_yaml('headers')['sn']
        add_data['paperNum'] = 1

    response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                               json=glu_data)

    if response['data']['count'] == 0:
        re.request_main('post', Url.TEMP_ADD, headers=read_yaml('headers'),
                        json=add_data)

    response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                               json=glu_data)

    write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_TEMP_INFO'])
