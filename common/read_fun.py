# coding=UTF-8
import os
import sys
import jinja2
from common.read_yaml import load
from common.com import Ran
import time
import datetime
from testCase.get_basic import qc_record
from config.contast import Path

sys.path.append(r'' + os.path.abspath('../'))


class LoadBasic(object):
    """
    加载headers文件的内容包含登陆的账号信息，请求头 等
    """

    @staticmethod
    def read_user_info():
        return load(Path.path['basic']['HEADER_PATH'])

    '''
    加载患者信息
    '''

    @staticmethod
    def read_patient_info():
        return load(Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])

    '''/
    加载患者血糖信息
    '''

    @staticmethod
    def read_blood_info():
        return load(Path.path['basic']['INHOS_PATIENT_BLOOD_INFO'])

    '''
    加载医嘱信息
    '''

    @staticmethod
    def read_order_info():
        return load(Path.path['basic']['ORDER_INFO'])

    @staticmethod
    def read_temp_blood_info():
        return load(Path.path['basic']['INHOS_TEMP_INFO'])

    @staticmethod
    def read_sn_info():
        return load(Path.path['basic']['SN_INFO'])

    @staticmethod
    def read_paper_info():
        return load(Path.path['basic']['PAPER_INFO'])

    @staticmethod
    def read_liquid_info():
        return load(Path.path['basic']['LIQUID_INFO'])

    @staticmethod
    def read_qc_info():
        return load(Path.path['basic']['QC_INFO'])

    @staticmethod
    def read_mz_patient_info():
        return load(Path.path['basic']['MZ_PATIENT_INFO'])


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(**kwargs)


# yaml 文件调用以下函数


'''
获取当前时间
'''


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


'''
获取当天0点和23:59
'''


def get_start_end_time():
    list = {}
    endTime = time.strftime("%Y-%m-%d 23:59:59", time.localtime())
    startTime = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    list['startTime'] = startTime
    list['endTime'] = endTime
    return list


'''
获取7天前的日期
'''


def start_time():
    yes_time_nyr = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:00")
    return yes_time_nyr


def read_basic_info():
    dict = {}
    dict['sn'] = LoadBasic.read_sn_info()
    dict['paper_info'] = LoadBasic.read_paper_info()
    dict['user_info'] = LoadBasic.read_user_info()
    dict['inhos_patient_info'] = LoadBasic.read_patient_info()
    dict['inhos_patient_blood_info'] = LoadBasic.read_blood_info()
    dict['inhos_temp_info'] = LoadBasic.read_temp_blood_info()
    dict['order_info'] = LoadBasic.read_order_info()
    dict['qc_info'] = LoadBasic.read_qc_info()

    return dict


'''
读取yaml文件
'''

def read_yaml_info(path):
    r = render(path,
               **{"phone": Ran().phoneNORandomGenerator, 'card': Ran().ran_end,
                  "get_time": get_time, "num": Ran().number, "get_start_end_time": get_start_end_time,
                  "start_time": start_time,
                  'read_basic_info': read_basic_info, 'qc_add': qc_record.qc_add})
    return r
