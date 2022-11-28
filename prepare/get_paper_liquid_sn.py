# coding=UTF-8
import os
import sys
from testCase.log import logger
from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Path
from common.http_client import RequestMain
import datetime

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_paper_liquid_sn():
    if read_yaml('headers')["Platform"] == '1':
        paper_url = Url.PAPER + '/number'
        liquild_url = Url.LIQUID + '/number'
        logger.log_info.info("获取试纸质控液数据")
        paper = re.request_main('post', paper_url, headers=read_yaml('headers'),
                                )['data']

        liquid = re.request_main('post', liquild_url, headers=read_yaml('headers'),
                                 )['data']

    else:
        paper_url = Url.PAPER
        liquild_url = Url.LIQUID
        logger.log_info.info("获取试纸质控液设备数据")
        paper = re.request_main('post', paper_url, headers=read_yaml('headers'),
                                json={"pageNo": 1,
                                      "pageSize": 15})['data']
        if paper['count'] == 0:
            paper = []
        else:
            paper = paper['lists']

        liquid = re.request_main('post', liquild_url, headers=read_yaml('headers'),
                                 json={"pageNo": 1,
                                       "pageSize": 15})['data']
        if liquid['count'] == 0:
            liquid = []
        else:
            liquid = liquid['lists']

        sn = re.request_main('post', Url.SN, headers=read_yaml('headers'),
                             json={"pageNo": -1, 'pageSize': 10})['data']
        if sn['count'] == 0:
            sn = []
        else:
            sn = sn['lists']

        if len(sn) == 0:
            logger.log_info.info("该账号下无设备")
            return False
        else:
            l1 = []
            for i in sn:
                if i['devStatus'] == 0:
                    l1.append(i)
            write_yaml(l1, Path.path['basic']['SN_INFO'])
            logger.log_info.info("设备获取完毕")

    if len(liquid) == 0:
        logger.log_info.info("该账号下无质控液")
        return False
    else:
        l2 = []
        for i in liquid:
            b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
            if b >= datetime.datetime.now():
                l2.append(i)
        write_yaml(l2, Path.path['basic']['LIQUID_INFO'])
        logger.log_info.info("质控液获取完毕")

    if len(paper) == 0:
        logger.log_info.info("该账号下无试纸")
        return False
    else:
        l3 = []
        for i in paper:

            b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
            if b >= datetime.datetime.now():
                l3.append(i)
        write_yaml(l3, Path.path['basic']['PAPER_INFO'])
        logger.log_info.info("试纸获取完毕")

    return True
