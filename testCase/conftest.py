# coding=UTF-8
import os
import sys

sys.path.append(r'' + os.path.abspath('../'))
import pytest
import requests
from common.yaml_util import clear_yaml,write_yaml,read_yaml,clear_menzhen_yaml,read_url_csv,write_menzhen_yaml
from data import menzhen_patient,menzhen_blood
from testCase.log import logger

url = read_url_csv()[0]

from common.yaml_util import read_csv


@pytest.fixture(scope='function')
def login():
    l = []
    try:
        response = requests.post(url.format('login'), headers=menzhen_patient.getheader(), data=menzhen_patient.login(read_csv()[0],
                                                                                                                      read_csv()[1]))
    except:
        logger.getlogger().error("登陆报错检测是不是服务没起，还是账号密码错误")

    headers = menzhen_patient.getheader()

    headers["Access-Token"] = response.json()['data']['accessToken']
    headers["refresh_token"] = response.json()['data']['refreshToken']
    write_yaml({'headers':headers})
    if response.status_code == 200:
        info = response.json()['data']["permissions"]
        for i in info:
            l.append(i['dcrp'])
        write_yaml({"permissions":l})
    return headers
if "门诊管理" in read_yaml('permissions'):
    @pytest.fixture(scope='function')
    def in_patient(login):
        response = requests.post(url.format('mz/patient/list'), headers=read_yaml('headers'),
                                 data=menzhen_patient.in_patient()).json()
        print('aa')
        if response['data']['count'] != 0:
            write_menzhen_yaml(response['data']['lists'][0])
        else:
            logger.getlogger().debug('没有数据，请先添加一位患者')
            assert 1 == 2
        try:
            assert response['code'] == 0
            assert response['msg'] == '请求成功'

        except AssertionError:
            logger.getlogger().error("登陆后台 %s", "接口报错", exc_info=1)
            assert response['code'] == 0
        return response['data']['lists'][0]






@pytest.fixture(scope='session',autouse=True)
def excute_dabates_sql():
    clear_yaml()
    clear_menzhen_yaml()
    yield



