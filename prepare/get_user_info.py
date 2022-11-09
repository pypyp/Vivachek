# coding=UTF-8
import os
import sys

from common.yaml_util import write_yaml, read_yaml

from config.contast import Url, Header, Path, Client_Header, Config
from common.httpClient import RequestMain

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_user_info():
    global header
    info = Config.info
    type = info['type']
    if type == 1:
        info['login']['sn'] = Client_Header.header['sn']
        header = Client_Header.header

    elif type == 3:
        header = Header.header


    # logger.log_info.info("登陆,获取token以及账号的一些基础信息")

    response = re.request_main('post', Url.LOGIN, headers=header, json=info['login'])
    if response['code'] != 0:
        print('账号密码错误')
        return False
    else:
        header["Access-Token"] = response['data']['accessToken']
        header["refresh_token"] = response['data']['refreshToken']
        write_yaml({'headers': header}, Path.path['basic']['HEADER_PATH'])
        write_yaml({"userId": response['data']["userId"]}, Path.path['basic']['HEADER_PATH'])

        if info['login']['hisId'] == 'vivachek':
            dept = re.request_main('post', Url.DEPT, headers=read_yaml('headers'),
                                   json={"inhos": 1})
            l = []
            for i in dept['data']:
                l.append(i['id'])
            write_yaml({"deptId": l[0]}, Path.path['basic']['HEADER_PATH'])
            write_yaml({"auth": l}, Path.path['basic']['HEADER_PATH'])
        write_yaml({"deptId": response['data']['deptId']}, Path.path['basic']['HEADER_PATH'])
        write_yaml({"auth": response['data']['dataAuthIds']}, Path.path['basic']['HEADER_PATH'])
        write_yaml({"hosId": response['data']["hosId"]}, Path.path['basic']['HEADER_PATH'])
        info = response['data']["permissions"]
        l = []
        for i in info:
            l.append(i['id'])
        write_yaml({"permissions": l}, Path.path['basic']['HEADER_PATH'])
        return True
