import os
import sys

sys.path.append(r'' + os.path.abspath('../../'))
import allure
import pytest, yaml
# from data.read_fun import read_yaml_info
import requests
from testCase.log import logger
from common.yaml_util import read_bastase_sql, read_yaml
from common.open_database import MysqlDb
import json
from common.read_yaml import load
from compare.encapsulation import Encapsulation
from config.contast import Url, Path
from compare import dept, timeType, sysPrintInfo
from common.httpClient import RequestMain

re = RequestMain()


@allure.feature('配置接口')
class TestCommon(object):
    @allure.title('科室查询')
    @pytest.mark.parametrize('info', load(Path.path["DEPT"]))
    def test_dept(self, info):
        response = re.request_main('post', Url.DEPT, headers=read_yaml('headers'),
                                   json=info['parame'])
        Encapsulation.repeatOne(Url.DEPT, info, response, dept.Dept.schema)

    # @allure.title('医护人员查询')
    # @pytest.mark.parametrize('info',
    #                          yaml.safe_load(read_yaml_info(load('../data/path/path.yaml')['dept'])))
    # def test_time_type(self, info):
    #     if read_yaml('headers')['Platform'] == str(3):
    #         response = requests.post(Url.SYSTEM_TIME_WEB_INFO, headers=read_yaml('headers'),
    #                                  data=json.dumps(info['parame']), timeout=60).json()
    #         Encapsulation.repeatOne(Url.SYSTEM_TIME_WEB_INFO, read_yaml('headers'), info, response,
    #                                 timeType.TimeType.webView())
    #     else:
    #         response = requests.post(Url.SYSTEM_TIME_INFO, headers=read_yaml('headers'),
    #                                  data=json.dumps(info['parame']), timeout=60).json()
    #         Encapsulation.repeatOne(Url.SYSTEM_TIME_INFO, read_yaml('headers'), info, response,
    #                                 timeType.TimeType.schema)
    #
    # def test_print_info(self):
    #     info = {
    #         "result": {"msg": "请求成功",
    #                    "code": 0}
    #
    #     }
    #     if read_yaml('headers')['Platform'] == str(1):
    #         response = requests.post(Url.SYSTEM_PRINT_INFO, headers=read_yaml('headers'), timeout=60).json()
    #         Encapsulation.repeatOne(Url.SYSTEM_TIME_WEB_INFO, read_yaml('headers'), info, response,
    #                                 sysPrintInfo.SysPrintInfo.schema)
