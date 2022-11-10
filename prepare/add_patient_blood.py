# coding=UTF-8
import os
import sys
import time
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.httpClient import RequestMain
from testCase.log import logger

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def add_patient_blood(userid):
    data = {
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
        data["method"] = 1
        data['deviceNo'] = read_yaml('headers')['sn']
        data['paperNum'] = 1
    logger.log_info.info("添加患者血糖")
    response = re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
                               json=data)

    if response["code"] == 0:
        logger.log_info.info("血糖添加成功")
        return True

