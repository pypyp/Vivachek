# coding=UTF-8
import os
import sys
import jinja2
from common.read_yaml import load
from common.com import Ran
import time
import datetime
from prepare.add_qc import qc_data
from config.contast import Path

sys.path.append(r'' + os.path.abspath('../'))


class LoadBasic(object):
    """
        加载headers文件的内容包含登陆的账号信息，请求头 等
    """

    @staticmethod
    def read_user_info():
        """
            加载登陆用户信息
        """
        return load(Path.path['basic']['HEADER_PATH'])

    @staticmethod
    def read_patient_info():
        """
            加载患者信息
        """
        return load(Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])

    @staticmethod
    def read_blood_info():
        """
            加载患者血糖信息
        """

        return load(Path.path['basic']['INHOS_PATIENT_BLOOD_INFO'])

    @staticmethod
    def read_order_info():
        """
            加载医嘱信息
        """
        return load(Path.path['basic']['ORDER_INFO'])

    @staticmethod
    def read_temp_blood_info():
        """
            加载临时检测信息
        """
        return load(Path.path['basic']['INHOS_TEMP_INFO'])

    @staticmethod
    def read_sn_info():
        """
            加载设备信息
        """
        return load(Path.path['basic']['SN_INFO'])

    @staticmethod
    def read_paper_info():
        """
            加载试纸信息
        """
        return load(Path.path['basic']['PAPER_INFO'])

    @staticmethod
    def read_liquid_info():
        """
            加载质控液信息
        """
        return load(Path.path['basic']['LIQUID_INFO'])

    @staticmethod
    def read_qc_info():
        """
            加载质控信息
        """
        return load(Path.path['basic']['QC_INFO'])

    @staticmethod
    def read_mz_patient_info():
        """
            加载门诊患者信息
        """
        return load(Path.path['basic']['MZ_PATIENT_INFO'])


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(**kwargs)


def get_time():
    """
       return：当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_start_end_time():
    """
       return：
       startTime:%Y-%m-%d 23:59:59
       endTime:Y-%m-%d 00:00:00
    """
    my_dict = {}
    endTime = time.strftime("%Y-%m-%d 23:59:59", time.localtime())
    startTime = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    my_dict['startTime'] = startTime
    my_dict['endTime'] = endTime
    return my_dict


def start_time():
    """
        return：获取7天前的日期
    """
    yes_time_nyr = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:00")
    return yes_time_nyr


def read_basic_info():
    """
        return：LoadBasic中的配置信息
    """

    my_dict_data = {'sn': LoadBasic.read_sn_info(), 'paper_info': LoadBasic.read_paper_info(),
                    'user_info': LoadBasic.read_user_info(), 'inhos_patient_info': LoadBasic.read_patient_info(),
                    'inhos_patient_blood_info': LoadBasic.read_blood_info(),
                    'inhos_temp_info': LoadBasic.read_temp_blood_info(), 'order_info': LoadBasic.read_order_info(),
                    'qc_info': LoadBasic.read_qc_info()}

    return my_dict_data


def read_yaml_info(path):
    """
    return：yaml文件输入
    """
    r = render(path,
               **{"phone": Ran().phone, 'card': Ran().ran_end,
                  "get_time": get_time, "num": Ran().number, "get_start_end_time": get_start_end_time,
                  "start_time": start_time,
                  'read_basic_info': read_basic_info, 'qc_add': qc_data})
    return r
