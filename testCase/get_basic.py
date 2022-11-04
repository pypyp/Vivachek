import json
from common.yaml_util import \
    read_yaml
from common.read_yaml import load
from config.contast import Path
import time, random

'''
此类用于获取在线门诊第一个患者的个人信息和第一条血糖数据
'''


class mz(object):
    @staticmethod
    def get_patient_info():
        data = json.dumps({"pageNo": 1, "pageSize": 21, "day": 1})
        return data

    @staticmethod
    def add_glu(userId):  # 添加血糖
        data = json.dumps({
            "userId": userId,
            "value": 6.2,
            "valueUnit": 1,
            "method": 0,
            "nurseId": read_yaml('userId'),
            "timeType": "q2h",
            "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "unusual": 2,
            'comment': '添加'
        })
        return data

    @staticmethod
    def get_blood_info(userId):
        data = json.dumps({
            "userId": userId,
            "pageNo": 1,
            "orderBy": "id desc",
            "pageSize": 20
        })
        return data


class zy(object):
    @staticmethod
    def get_patient_info():
        data = {"pageNo": 1, "pageSize": 15}
        return data

    @staticmethod
    def add_glu(userId):  # 添加血糖
        data = {
            "userId": userId,
            "value": 6.2,
            "valueUnit": 1,
            "method": 0,
            "nurseId": read_yaml('userId'),
            "timeType": "q2h",
            "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "unusual": 1,
            "comment": 'cs'
        }
        if "sn" in read_yaml('headers').keys():
            data["method"] = 1
            data['deviceNo'] = read_yaml('headers')['sn']
            data['paperNum'] = 1

        return data

    @staticmethod
    def get_blood_info(userId):
        data = {
            # "userId": (read_zy_yaml()['userId']),
            "userId": userId,
            "pageNo": 1,
            "orderBy": "id desc",
            "pageSize": 20
        }
        return data

    @staticmethod
    def alarm_list():
        data = json.dumps({
            # "deptId": read_zy_yaml()['deptId'],
            "pageNo": 1,
            "pageSize": 20
        })

    @staticmethod
    def get_order():
        data = {
            "pageNo": 1,
            "pageSize": 15,
            "endTime": time.strftime("%Y-%m-%d 23:59:59", time.localtime()),
            "startTime": time.strftime("%Y-%m-%d 00:00:00", time.localtime())
            # "deptId": read_zy_yaml()['deptId']
        }

        if "sn" in read_yaml('headers').keys():
            data = {
                "timeType": "午餐后"
            }
        return data

    @staticmethod
    def add_order(userId):
        data = json.dumps({
            "userId": userId,
            "type": 0,
            "timeType": "q2h",
            "startTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "entrust": ""})
        return data


class zy_temp(object):

    @staticmethod
    def tmep_glu_list():  # 获取临时检测血糖列表
        data = {
            "endtTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "startTime": time.strftime("%Y-%m-%d 00:00:00", time.localtime())

        }
        if "sn" in read_yaml('headers').keys():
            data = {}
        return data

    @staticmethod
    def add_glu():  # 添加血糖
        data = {
            "value": 6.2,
            "valueUnit": 1,
            "method": 0,
            "nurseId": read_yaml('userId'),
            "timeType": "q2h",
            "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "unusual": 1
        }

        if "sn" in read_yaml('headers').keys():
            data["method"] = 1
            data['deviceNo'] = read_yaml('headers')['sn']
            data['paperNum'] = 1

        return data


class qc_record(object):
    @staticmethod
    def qc_add():
        value = 15.3
        liquid = random.choice(load(Path.path['basic']['LIQUID_INFO']))
        paper = random.choice(load(Path.path['basic']['PAPER_INFO']))
        sn = random.choice(load(Path.path['basic']['SN_INFO']))

        if liquid['type'] == 0:
            if value < paper['lowMinLimit'] or value > paper['lowMaxLimit']:
                result = 1
            else:
                result = 0

        elif liquid['type'] == 1:
            if value < paper['mediumMinLimit'] or value > paper['mediumMaxLimit']:
                result = 1
            else:
                result = 0
        else:
            if value < paper['mediumMinLimit'] or value > paper['mediumMaxLimit']:
                result = 1
            else:
                result = 0
        data = {
            "value": value,
            "sn": sn['sn'],
            "liquidId": liquid['id'],
            'paperId': paper['id'],
            "measureTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "result": result,
        }
        return data
