from testCase.offline_basic import basic
import path


def get_url(type, ip, port):
    if type == 3:
        port = int(port) + 1000
        url = "http://" + ip + ":" + str(port) + "/vivachekcloud/api/"
        return url

    else:
        url = "http://" + ip + ":" + str(port) + "/vivachekcloud/"
        return url


class Config(object):
    """
    登陆用户信息
    type：1客户端
          3网页端
    """

    TYPE = 1
    IP = "47.111.0.135"
    PORT = '10192'
    info = {
        "type": TYPE,
        "url":get_url(TYPE, IP, PORT),
        "login": {
            "hisId": "8036",
            "password": "123456",
        }
    }

    """
    测试服数据库地址配置
    """
    database = {
        "MYSQL_HOST": "47.111.0.135",
        "MYSQL_PORT": 3306,
        "MYSQL_USER": "root",
        "MYSQL_PASSWD": "Nov2014",
        "database": " `vivachekcloud_cdwy`"}


"""
测试服接口地址
"""


class Url(object):
    info = Config.info
    url = info['url']
    BASE_URL = url
    LOGIN = url + "login"
    REFRESH_TOKEN = "getToken"
    USER_INFO = url + "getUserInfo"
    DEPT = url + "common/dept/list"
    SYSTEM_TIME_INFO = url + "system/time/info"
    SYSTEM_TIME_WEB_INFO = url + "system/time/web_viewInfo"
    SYSTEM_PRINT_INFO = url + "system/print/info"
    PATIENT_LIST = url + "inhos/patient/list"
    PATIENT_LEAVE = url + "inhos/patient/list/leave"
    PATIENT_INFO = url + "inhos/patient/info"
    HEALTH_ARCHIVES = url + 'inhos/patient/healthArchives/info'
    CHANGE_BED = url + 'inhos/patient/changebed'
    PATIENT_UPDATE = url + 'inhos/patient/update'
    PATIENT_ADD = url + 'inhos/patient/add'
    SCAN = url + "inhos/patient/info/scan"
    GLU_ADD = url + 'inhos/glu/add'
    GLU_LIST = url + "inhos/glu/list"
    GLU_REPORT = url + "inhos/glu/report"
    GLU_INFO = url + "inhos/glu/info"
    PATIENTTRENDCHART = url + 'inhos/glu/patientTrendChart'
    PATIENTPIECHART = url + 'inhos/glu/patientPieChart'
    GLU_UPDATE = url + 'inhos/glu/update'
    GLU_DEL = url + 'inhos/glu/delete'
    WEB_MONITORLIST = url + 'inhos/measure/glu_order/web_monitorList'
    ADD_MEASURE = url + 'inhos/measure/glu_order/addMeasure'
    ORDER_UPDATE = url + 'inhos/measure/glu_order/update'
    ORDER_STOP = url + 'inhos/measure/glu_order/stop'
    APP_MONITORLIST = url + 'inhos/measure/glu_order/monitorList'
    PATIENT_ORDER = url + "inhos/measure/glu_order/getPatientOrderList"
    PATIENT_ORDER_INFO = url + 'inhos/measure/glu_order/info'
    MEASURE_LIST = url + "inhos/glu/app_measureGluList"
    TASK = "inhos/measure/glu_order/monitorList"
    TEMP_LIST = url + "inhos/measure/temp/list"
    TEMP_ADD = url + 'inhos/measure/temp/add'
    TEMP_UPDATE = url + 'inhos/measure/temp/update'
    TEMP_DEL = url + 'inhos/measure/temp/delete'
    EXTERNAL_LIST = "qc/record/external/app/list"
    PAPER = url + "paper/list"
    LIQUID = url + "qc/liquid/list"
    SN = url + "device/list"
    QC_LIST = url + "qc/record/list"
    QC_ADD = url + "qc/record/add"
    QC_UPDATE = url + "qc/record/update"
    QC_DELETE = url + "qc/record/delete"
    QC_ANALYSIS = url + "qc/record/analysis"
    QC_STATISTICS = url + "qc/record/statistics"


"""
web端请求头
"""


class Header(object):
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Project": "vivachekcloud",
        "Platform": "3",
        "Version": "v1.7.0",
        "X-User-Agent": "ios/8.1",
        "Connection": "keep-alive"
    }


"""
web端请求头
"""


class Client_Header(object):
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Project": "vivachekcloud",
        "Platform": "1",
        "Version": "v1.3.3",
        "X-User-Agent": "t9801/30",
        "Connection": "keep-alive",
        "sn": '359B0000064'

    }


"""
离线请求头
"""


class Offline_Header(object):
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Project": "vivachekcloud",
        "Platform": "1",
        "Version": "v1.7.0",
        "X-User-Agent": "ios/8.1",
        "Connection": "keep-alive",
        "sn": '359B0000064',
        "TimeStampReq": basic.get_unixtime(),
        "Nonce": basic.get_Nonce()

    }


ROOT_PATH = path.get_project_path() + '\\data'

"""
每个测试接口测试用力存放地址
"""


class Path(object):
    path = {"basic":
                {"HEADER_PATH": ROOT_PATH + "\\basic_info\\headers\\extract.yaml",
                 "INHOS_PATIENT_BASIC_INFO": ROOT_PATH + "\\basic_info\\inhos_patient_info\\zy.basic.yaml",
                 "INHOS_PATIENT_BLOOD_INFO": ROOT_PATH + "\\basic_info\\inhos_patient_blood_info\\blood_info.yaml",
                 "INHOS_TEMP_INFO": ROOT_PATH + "\\basic_info\\temp_blood_info\\temp_blood.yaml",
                 "ORDER_INFO": ROOT_PATH + "\\basic_info\\order_info\\order_info.yaml",
                 "PAPER_INFO": ROOT_PATH + "\\basic_info\\sn_paper_liquid_info\\paper_info.yaml",
                 "LIQUID_INFO": ROOT_PATH + "\\basic_info\\sn_paper_liquid_info\\liquid_info.yaml",
                 "SN_INFO": ROOT_PATH + "\\basic_info\\sn_paper_liquid_info\\sn_info.yaml",
                 "QC_INFO": ROOT_PATH + "\\basic_info\\qc_info\\qc_info.yaml",
                 "MZ_PATIENT_INFO": ROOT_PATH + "\\basic_info\\mz_patient_info\\mz_patient_info.yaml",
                 "MZ_PATIENT_BLOOD_INFO": ROOT_PATH + "\\basic_info\\mz_patient_blood_info\\mz_patient_blood_info.yaml"

                 },
            "DEPT": ROOT_PATH + "\\commom\\dept.yaml",
            "USER": ROOT_PATH + "\\commom\\user.yaml",
            "INHOS_PATIENT_LIST": ROOT_PATH + "\\inhos_patient\\inhos_patient_list.yaml",
            "INHOS_PATIENT_LIST_LEAVE": ROOT_PATH + "\\inhos_patient\\inhos_patient_list_leave.yaml",
            "INHOS_PATIENT_INFO": ROOT_PATH + "\\inhos_patient\\inhos_patient_info.yaml",
            "INHOS_PATIENT_INFO_HEALTHARCHIVES": ROOT_PATH + "\\inhos_patient\\inhos_patient_info_healthArchives.yaml",
            "INHOS_PATIENT_CHANGEBED": ROOT_PATH + "\\inhos_patient\\inhos_patient_changebed.yaml",
            "INHOS_PATIENT_UPDATE": ROOT_PATH + "\\inhos_patient\\inhos_patient_update.yaml",
            "INHOS_PATIENT_ADD": ROOT_PATH + "\\inhos_patient\\inhos_patient_add.yaml",
            "INHOS_PATIENT_LEAVE": ROOT_PATH + "\\inhos_patient\\inhos_patient_leave.yaml",
            "INHOS_GLU_ADD": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_add.yaml",
            "INHOS_GLU_DEL": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_del.yaml",
            "INHOS_GLU_LIST": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_list.yaml",
            "INHOS_GLU_INFO": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_info.yaml",
            "INHOS_GLU_UPDATE": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_update.yaml",
            "INHOS_GLU_PATIENTPIECHART": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_patientPieChart.yaml",
            "INHOS_GLU_PATIENTTRENDCHART": ROOT_PATH + "\\inhos_patient_blood\\inhos_glu_patientTrendChart.yaml",
            "INHOS_MEASURE_TEMP_ADD": ROOT_PATH + "\\temp_blood\\inhos_measure_temp_add.yaml",
            "INHOS_MEASURE_TEMP_UPDATE": ROOT_PATH + "\\temp_blood\\inhos_measure_temp_update.yaml",  # 更新临时检测血糖
            "INHOS_MEASURE_TEMP_LIST": ROOT_PATH + "\\temp_blood\\inhos_measure_temp_list.yaml",  # 临时检测血糖列表
            "INHOS_MEASURE_TEMP_DELETE": ROOT_PATH + "\\temp_blood\\inhos_measure_temp_delete.yaml",  # 删除临时检测
            "QC_RECORD_LIST": ROOT_PATH + "\\qc\\qc_record_list.yaml",  # 质控查询
            "QC_RECORD_ADD": ROOT_PATH + "\\qc\\qc_record_add.yaml",  # 质控添加
            "QC_RECORD_UPDATE": ROOT_PATH + "\\qc\\qc_record_update.yaml",  # 质控更新
            "QC_RECORD_DELETE": ROOT_PATH + "\\qc\\qc_record_delete.yaml",  # 质控删除
            "QC_RECORD_STATISTICS": ROOT_PATH + "\\qc\\qc_record_statistics.yaml",  # 质控统计
            "QC_RECORD_ANALYSIS": ROOT_PATH + "\\qc\\qc_record_analysis.yaml",  # 质控分析

            "ADD_MEASURE": ROOT_PATH + "\\order\\glu_order_addMeasure.yaml",  # web检测任务列表
            "ORDER_LIST": ROOT_PATH + "\\order\\inhos_measure_glu_order_Web_OrderList.yaml",  # web检测任务列表
            "PATIENT_ORDER_LIST": ROOT_PATH + "\\order\\inhos_measure_glu_order_getPatientOrderList.yaml",  # web检测任务列表
            "ORDER_INFO": ROOT_PATH + "\\order\\inhos_measure_glu_order_info.yaml",  # web检测任务详情
            "ORDER_UPDATA": ROOT_PATH + "\\order\\inhos_measure_glu_order_update.yaml",  # 检测任务更新
            "ORDER_STOP": ROOT_PATH + "\\order\\inhos_measure_glu_order_stop.yaml",  # 检测任务更新

            }

# 返回响应结果
