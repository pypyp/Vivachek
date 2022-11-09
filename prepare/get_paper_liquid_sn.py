# coding=UTF-8
import os
import sys
from testCase.log import logger
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.httpClient import RequestMain
import datetime

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_paper_liquid_sn():
    if read_yaml('headers')["Platform"] == '1':
        paper_url = Url.PAPER + '/number'
        liquild_url = Url.LIQUID + '/number'
        paper = re.request_main('post', paper_url, headers=read_yaml('headers'),
                                )
        liquid = re.request_main('post', liquild_url, headers=read_yaml('headers'),
                                 )

    else:
        paper_url = Url.PAPER
        liquild_url = Url.LIQUID
        paper = re.request_main('post', paper_url, headers=read_yaml('headers'),
                                json={"pageNo": 1,
                                      "pageSize": 15})
        liquid = re.request_main('post', liquild_url, headers=read_yaml('headers'),
                                 json={"pageNo": 1,
                                       "pageSize": 15})

        sn = re.request_main('post', Url.SN, headers=read_yaml('headers'),
                             json={"pageNo": -1, 'pageSize': 10})

        l1 = []
        try:
            for i in sn['data']['lists']:
                if i['devStatus'] == 0:
                    l1.append(i)
            write_yaml(l1, Path.path['basic']['SN_INFO'])
        except Exception as e:
            logger.log_info.error("获取设备信息报错---->%s"%e.args)
            return False
    try:
        l2 = []
        for i in liquid['data']['lists']:
            b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
            if b >= datetime.datetime.now():
                l2.append(i)
                # break
        write_yaml(l2, Path.path['basic']['LIQUID_INFO'])
    except Exception as e:
        logger.log_info.error("获取质控液信息报错---->%s"%e.args)
        return False
    try:
        l3 = []
        for i in paper['data']['lists']:
            b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
            if b >= datetime.datetime.now():
                l3.append(i)
                # break
        write_yaml(l3, Path.path['basic']['PAPER_INFO'])
    except Exception as e:
        logger.log_info.error("获取试纸信息报错---->%s"%e.args)
        return False
    return True
