# coding=UTF-8
import os
import sys
from testCase.log import logger
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url,  Path
from common.http_client import RequestMain


sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_patient_info():
    data = {"pageNo": 1, "pageSize": 15}
    logger.log_info.info("根据登陆账号权限获取一个患者的信息")
    response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                               json=data)
    if response['data']['count'] == 0:

        logger.log_info.info("该登陆账号下没有患者")
        return None
    else:
        info = re.request_main('post', Url.PATIENT_INFO, headers=read_yaml('headers'),
                               json={"userId": response['data']['lists'][0]['userId']})
        write_yaml(info['data'], Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])
        userid = info['data']['userId']
        ipt_time = info['data']['iptTime']
        logger.log_info.info("患者信息获取完毕")
        return userid,ipt_time
