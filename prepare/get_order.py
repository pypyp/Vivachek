# coding=UTF-8
import os
import sys
import time

from common.open_database import MysqlDb
from common.yaml_util import write_yaml, read_yaml, read_bastase_sql

from config.contast import Url, Path, Config
from common.httpClient import RequestMain
from datetime import datetime

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()


def get_order():
    if read_yaml('headers')["Platform"] == '1':
        order = Url.APP_MONITORLIST

    else:

        order = Url.WEB_MONITORLIST
        order_data = {
            "pageNo": 1,
            "pageSize": 15,
            "endTime": time.strftime("%Y-%m-%d 23:59:59", time.localtime()),
            "startTime": time.strftime("%Y-%m-%d 00:00:00", time.localtime())

        }

    response = re.request_main('post', order, headers=read_yaml('headers'),
                               json=order_data)
    write_yaml({'analysisModel': response['data']['analysisModel']}, Path.path['basic']['ORDER_INFO'])
    if order == Url.WEB_MONITORLIST:
        id = response['data']['lists'][0]['id']
        data = MysqlDb().select_db(
            "select * from {}.`medical_order_detail`where id=\'{}\' ".format(Config.database['database'],
                                                                             id))
        if response['data']['analysisModel'] == 0:
            write_yaml(response['data']['lists'][0], Path.path['basic']['ORDER_INFO'])
            write_yaml({'orderid': data[0]['order_id']}, Path.path['basic']['ORDER_INFO'])
        if response['data']['analysisModel'] == 1:
            for i in response['data']['lists']:
                if i['status'] == 1:
                    write_yaml(i, Path.path['basic']['ORDER_INFO'])
                    write_yaml({'orderid': data[0]['order_id']}, Path.path['basic']['ORDER_INFO'])
                    break
    else:
        if "tasks" in response['data'].keys():
            write_yaml(response['data']['tasks'][0], Path.path['basic']['ORDER_INFO'])
        else:
            write_yaml(response['data']['taskLookupList'][0]['tasks'][0], Path.path['basic']['ORDER_INFO'])
