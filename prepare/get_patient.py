# coding=UTF-8
import os
import sys
import time
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Header, Path, Client_Header, Config
from common.httpClient import RequestMain
from prepare.get_basic import zy

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_patient_info():
    data = {"pageNo": 1, "pageSize": 15}
    response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                               json=data)
    if response['data']['count'] == 0:

        print("该账号下没有患者")
        return None
    else:
        info = re.request_main('post', Url.PATIENT_INFO, headers=read_yaml('headers'),
                               json={"userId": response['data']['lists'][0]['userId']})
        write_yaml(info['data'], Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])
        userid = info['data']['userId']
        ipt_time = info['data']['iptTime']

        return userid,ipt_time
