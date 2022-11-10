# coding=UTF-8
import os
import sys
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.httpClient import RequestMain
from datetime import datetime

from testCase.log import logger

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_blood_info(userid, ipt_time):
    data = {
        "userId": userid,
        "pageNo": 1,
        "orderBy": "measure_time desc",
        "pageSize": 20,
        "patGluStatus": 1

    }
    if read_yaml('headers')["Platform"] == '1':
        ipt_time = datetime.strptime(ipt_time, '%Y-%m-%d %H:%M:%S')
        ipt_time = ipt_time.strftime('%Y-%m-%d 00:00:00')
        data = {
            "userId": userid,
            "pageNo": 1,
            "pageSize": 20,
            "startTime": ipt_time,
            "endTime": datetime.now().strftime('%Y-%m-%d 23:59:59')

        }
    logger.log_info.info("获取该患者的一条血糖数据")
    response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                               json=data)

    if response['data']['count'] != 0:
        write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_PATIENT_BLOOD_INFO'])
        logger.log_info.info("患者的血糖数据获取完毕")
        return True
    logger.log_info.info("患者无血糖数据")
    return False
