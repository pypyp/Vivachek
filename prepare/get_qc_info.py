# coding=UTF-8
import os
import sys
from common.yaml_util import write_yaml, read_yaml
from config.contast import Url, Path
from common.httpClient import RequestMain
from testCase.log import logger

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_qc_info():
    data = {"pageNo": 1, 'pageSize': 20}

    if read_yaml('headers')["Platform"] == '1':
        data['sn'] = read_yaml('headers')["sn"]

    logger.log_info.info("获取质控数据")
    response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
                               json=data)
    if response['data']['count'] != 0:
        write_yaml(response['data']['lists'][0], Path.path['basic']['QC_INFO'])
        logger.log_info.info("质控数据获取完毕")
        return True
    logger.log_info.info("无质控数据")
    return False


