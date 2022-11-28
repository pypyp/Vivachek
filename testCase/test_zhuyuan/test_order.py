# coding=UTF-8
import os
import sys
import pytest
import allure
from common.yaml_util import read_yaml
from common.read_fun import read_yaml_info
from testCase.log import logger
import yaml
from common.open_database import MysqlDb
from config.contast import Url, Path, Config
from compare.encapsulation import Encapsulation
from compare import patienf_order, patient_ordr_info, web_order
from common.http_client import RequestMain

sys.path.append(r'' + os.path.abspath('../../'))
re = RequestMain()


@allure.feature('医嘱')
class Test_order(object):

    @allure.title('根据任务添加血糖')
    @pytest.mark.skipif(
        '1010202' not in read_yaml('permissions') and "20103" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ADD_MEASURE'])))
    def test_glu_order_addMeasure(self, info):
        if read_yaml('headers')['Platform'] == '3':
            if info["analysisModel"] == 0:
                logger.log_info.info('任务不解析')
            else:
                info['parame'].pop('deviceNo')
                response = re.request_main('post', Url.ADD_MEASURE, headers=read_yaml('headers'),
                                           json=info['parame'])

                data = MysqlDb().select_db(
                    "select * from {}.`blood_glucose_record` where measure_id=\'{}\'".format(
                        Config.database['database'],
                        info['parame']['id']))

                Encapsulation.repeatThree(Url.ADD_MEASURE, info, response)
                assert data[0]['value'] == info['parame']['value']

        else:
            info['parame']['method'] = 1
            info['parame']['deviceNo'] = read_yaml('headers')['sn']
            response = re.request_main('post', Url.ADD_MEASURE, headers=read_yaml('headers'),
                                       json=info['parame'])

            data = MysqlDb().select_db(
                "select * from {}.`blood_glucose_record` where measure_id=\'{}\'".format(Config.database['database'],
                                                                                         info['parame']['id']))

            Encapsulation.repeatThree(Url.ADD_MEASURE, info, response)
            assert data[0]['value'] == info['parame']['value']

    @allure.title('所有患者任务')
    @pytest.mark.skipif(
        '1010202' not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ORDER_LIST'])))
    def test_glu_order_webOrderList(self, info):
        if read_yaml('headers')['Platform'] == '3':

            response = re.request_main('post', Url.WEB_MONITORLIST, headers=read_yaml('headers'),
                                       json=info['parame'])
            Encapsulation.repeatOne(Url.WEB_MONITORLIST, info, response, web_order.WebOrder.get())
            if response['data']['totalPage'] > 1:
                old_list = response['data']['lists']
                for i in range(2, response['data']['totalPage'] + 1):
                    info['parame']['pageNo'] = i
                    response = re.request_main('post', Url.WEB_MONITORLIST, headers=read_yaml('headers'),
                                               json=info['parame'])
                    new_list = Encapsulation.repeatTwo(Url.WEB_MONITORLIST, info, response, old_list,
                                                       web_order.WebOrder.get())
                    old_list = new_list

    @allure.title('患者任务列表')
    @pytest.mark.skipif(
        '10101010204' not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['PATIENT_ORDER_LIST'])))
    def test_glu_order_getPatientOrderList(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.PATIENT_ORDER, headers=read_yaml('headers'),
                                       json=info['parame'])
            Encapsulation.repeatOne(Url.PATIENT_ORDER, info, response, patienf_order.PatientOrder.schema)

    @allure.title('任务详情')
    @pytest.mark.skipif(
        '1010101020403' not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ORDER_INFO'])))
    def test_glu_order_info(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.PATIENT_ORDER_INFO, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.PATIENT_ORDER_INFO, info, response, patient_ordr_info.PatientOrderInfo.schema)

    @allure.title('编辑任务')
    @allure.title('任务详情')
    @pytest.mark.skipif(
        '1010101020401' not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ORDER_UPDATA'])))
    def test_glu_order_update(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.ORDER_UPDATE, headers=read_yaml('headers'),
                                       json=info['parame'])

            data = MysqlDb().select_db(
                "select * from {}.`medical_order`order by id desc limit 1".format(Config.database['database'],
                                                                                  ))

            Encapsulation.repeatThree(Url.ORDER_UPDATE, info, response)
            assert data[0]['time_type'] == info['parame']['timeType']
            assert data[0]['entrust'] == info['parame']['entrust']

    @allure.title('停止任务')
    @pytest.mark.skipif(
        '1010101020402' not in read_yaml('permissions'),
        reason='该账号无此权限')

    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ORDER_STOP'])))
    def test_glu_order_stop(self, info):
        if read_yaml('headers')['Platform'] == str(3):

            response = re.request_main('post', Url.PATIENT_ORDER, headers=read_yaml('headers'),
                                       json=info['userid'])
            logger.log_info.info({'list': response['data']['list']})
            for i in response['data']['list']:
                if i['status'] == 1:
                    info['parame']['id'] = i['id']
                    response = re.request_main('post', Url.ORDER_STOP, headers=read_yaml('headers'),
                                               json=info['parame'])

                    data = MysqlDb().select_db(
                        "select * from {}.`medical_order`order by id desc ".format(Config.database['database'],
                                                                                   ))
                    Encapsulation.repeatThree(Url.ORDER_STOP, info, response)
                    assert data[0]['status'] == 3

                    break

    # @allure.title('停止任务')
    # @pytest.mark.skipif(
    #     '1010101020101' not in read_yaml('permissions'),
    #     reason='该账号无此权限')
    # @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['ORDER_STOP'])))
    #     def test_add(self):
    #         pass

