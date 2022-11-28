# coding=UTF-8
import os
import sys
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.http_client import RequestMain
from datetime import datetime

from testCase.log import logger

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_temp_blood_info():
    data = {
        "startTime": datetime.now().strftime('%Y-%m-%d 00:00:00'),
        "endTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    }

    if read_yaml('headers')["Platform"] == '1':
        logger.log_info.info("获取临时检测数据")
        response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                                   )

    else:
        logger.log_info.info("获取临时检测数据")
        response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                                   json=data)

    if response['data']['count'] != 0:
        write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_TEMP_INFO'])
        logger.log_info.info("临时检测数据获取完毕")
        return True

    else:
        logger.log_info.info("无临时检测数据")
        return False
