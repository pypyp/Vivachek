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


def get_blood_info(userid, ipt_time):
    glu_data = {
        "userId": userid,
        "pageNo": 1,
        "orderBy": "measure_time desc",
        "pageSize": 20,
        "patGluStatus": 1

    }
    add_data = {
        "userId": userid,
        "value": 6.2,
        "valueUnit": 1,
        "method": 0,
        "nurseId": read_yaml('userId'),
        "timeType": "q2h",
        "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "unusual": 1,
        "comment": 'cs'
    }
    if read_yaml('headers')["Platform"] == '1':
        ipt_time = datetime.strptime(ipt_time, '%Y-%m-%d %H:%M:%S')
        ipt_time = ipt_time.strftime('%Y-%m-%d 00:00:00')

        glu_data = {
            "userId": userid,
            "pageNo": 1,
            "pageSize": 20,
            "startTime": ipt_time,
            "endTime": datetime.now().strftime('%Y-%m-%d 23:59:59')

        }

        add_data["method"] = 1
        add_data['deviceNo'] = read_yaml('headers')['sn']
        add_data['paperNum'] = 1

    if '10101010201' not in read_yaml('permissions') and read_yaml('headers')['Platform'] == '3':
        glu_data["nurseId"] = 'vivachek'

    response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                               json=glu_data)

#
    if response['data']['count'] == 0:
        re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
                        json=add_data)
        response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                   json=glu_data)
    write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_PATIENT_BLOOD_INFO'])
