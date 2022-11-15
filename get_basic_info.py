from prepare import check_is_open, clear, get_user_info, get_patient, get_blood, add_patient_blood, get_temp_blood_info, \
    get_order_info, add_qc, get_paper_liquid_sn, get_qc_info, add_temp_blood

from config.contast import Config

from common.yaml_util import read_yaml
from testCase.log import logger
import pytest

"""
/**
* 获取当前登陆账号权限下的一些基础信息 
*/

"""



class BasicConfiguration(object):
    logger.log_info.info("开始自动化测试,判断测试服是否正常")
    result = check_is_open.check_is_open(Config.IP, int(Config.PORT))
    if result is True:
        clear.clear()
        get_user_info.get_user_info()
        if '10101' or '20101' in read_yaml('permissions'):
            patient_info = get_patient.get_patient_info()

            if patient_info is not None:
                if get_blood.get_blood_info(patient_info[0], patient_info[1]) is False:
                    if add_patient_blood.add_patient_blood(patient_info[0]) is True:
                        get_blood.get_blood_info(patient_info[0], patient_info[1])
                pytest.main(["-sv", './testCase/test_zhuyuan/test_patient_blood.py'])

        # if "1010202" or "20103" in read_yaml('permissions'):
        #     get_order_info.get_order()
        #
        # if "1010206" or "20104" in read_yaml('permissions'):
        #     if get_temp_blood_info.get_temp_blood_info() is False:
        #         if add_temp_blood.add_temp_blood_info() is True:
        #             get_temp_blood_info.get_temp_blood_info()
        # if "106" or "2050104" in read_yaml('permissions'):
        #     if get_paper_liquid_sn.get_paper_liquid_sn() is True:
        #         if get_qc_info.get_qc_info() is False:
        #             if add_qc.qc_add() is True:
        #                 get_qc_info.get_qc_info()
        #
        # logger.log_info.info("测试数据准备完毕")

    else:
        logger.log_info.info("服务异常")
