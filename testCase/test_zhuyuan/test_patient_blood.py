# coding=UTF-8
import os
import sys
import pytest
import allure
from common.read_fun import read_yaml_info
from common.yaml_util import read_yaml, read_url_csv, read_bastase_sql
from testCase.log import logger
from common.open_database import MysqlDb
import yaml
from compare.encapsulation import Encapsulation
from config.contast import Url, Path
from compare import gluList, gluInfo, patientTrendChart, patientPieChart
from common.httpClient import RequestMain

sys.path.append(r'' + os.path.abspath('../../'))

url = read_url_csv()[0]
re = RequestMain()


@allure.feature("住院患者血糖")
class Test_zy_blood(object):
    @allure.title('住院患者血糖列表')
    @allure.description('该接口写了2个用例,全部血糖和按时间查询')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_LIST'])))
    def test_zy_glu_list(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_LIST, info, response, gluList.GluList.get())
                if 'data' not in response.keys():
                    if response['data']['totalPage'] > 1:
                        old_list = response['data']['lists']
                        for i in range(2, response['data']['totalPage'] + 1):
                            info['parame']['pageNo'] = i
                            response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                                       json=info['parame'])
                            new_list = Encapsulation.repeatTwo(Url.GLU_LIST, info, response, old_list,
                                                               gluList.GluList.get())
                            old_list = new_list

        elif read_yaml('headers')['Platform'] == str(1):
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_LIST, read_yaml('headers'), info, response, gluList.GluList.get())
                if 'data' not in response.keys():
                    if response['data']['totalPage'] > 1:
                        old_list = response['data']['lists']
                        for i in range(2, response['data']['totalPage'] + 1):
                            info['parame']['pageNo'] = i
                            response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                                       json=info['parame'])
                            new_list = Encapsulation.repeatTwo(Url.GLU_LIST, info, response, old_list,
                                                               gluList.GluList.get())
                            old_list = new_list

    @allure.title('住院患者血糖报告')
    @allure.description('该接口写了2个用例,全部血糖和按时间查询')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_LIST'])))
    def test_zy_glu_report(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == 2 or info['version'] == 3:

                response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_REPORT, info, response, gluList.GluList.get())
                if 'data' not in response.keys():
                    if response['data']['totalPage'] > 1:
                        old_list = response['data']['lists']
                        for i in range(2, response['data']['totalPage'] + 1):
                            info['parame']['pageNo'] = i
                            response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                                       json=info['parame'])
                            new_list = Encapsulation.repeatTwo(Url.GLU_REPORT, info, response, old_list,
                                                               gluList.GluList.get())
                            old_list = new_list

        elif read_yaml('headers')['Platform'] == str(1):
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_REPORT, info, response, gluList.GluList.get())
                if 'data' not in response.keys():
                    if response['data']['totalPage'] > 1:
                        old_list = response['data']['lists']
                        for i in range(2, response['data']['totalPage'] + 1):
                            info['parame']['pageNo'] = i
                            response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                                       json=info['parame'])
                            new_list = Encapsulation.repeatTwo(Url.GLU_REPORT, info, response, old_list,
                                                               gluList.GluList.get())
                            old_list = new_list

    @allure.title('住院血糖详情')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_INFO'])))
    def test_glu_info(self, info):
        response = re.request_main('post', Url.GLU_INFO, headers=read_yaml('headers'),
                                   json=info['parame'])
        Encapsulation.repeatOne(Url.GLU_INFO, info, response, gluInfo.GluInfo.schema)

    # @allure.title('住院血糖添加')
    # @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_ADD'])))
    # @allure.description('该接口写了10个用例，正常血糖，25.5，0.6，以及各种状态')
    # def test_add_zy_blood(self, info):
    #     if read_yaml('headers')['Platform'] == str(3):
    #         response = re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
    #                                    json=info['parame'])
    #     else:
    #         info['parame']['deviceNo'] = read_yaml('headers')['sn']
    #         info['parame']['method'] = 1
    #
    #         response = re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
    #                                    json=info['parame'])
    #     Encapsulation.repeatThree(Url.GLU_ADD, info, response)
    #
    #     data = MysqlDb().select_db(
    #         "select * from {}.`blood_glucose_record` where  user_id=\'{}\' ORDER BY id DESC limit 1".format(
    #             read_bastase_sql()[4],
    #             info['parame']['userId']
    #         ))
    #     try:
    #         info['parame']['comment']
    #     except:
    #         info['parame']['comment'] = None
    #
    #     assert str(data[0]['measure_time']) == info['parame']['measureTime']
    #     assert data[0]['comment'] == info['parame']['comment']
    #     assert data[0]['unusual'] == info['parame']['unusual']
    #     logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_ADD)

    @allure.title('住院患者血糖趋势图')
    @pytest.mark.parametrize('info', yaml.safe_load(
        read_yaml_info(Path.path['INHOS_GLU_PATIENTTRENDCHART'])))
    def test_patientTrendChart(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.PATIENTTRENDCHART, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.PATIENTTRENDCHART, info, response,
                                        patientTrendChart.PatientTrendChart.schema)
        elif read_yaml('headers')['Platform'] == str(1):
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.PATIENTTRENDCHART, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.PATIENTTRENDCHART, info, response,
                                        patientTrendChart.PatientTrendChart.schema)

    @allure.title('住院患者血糖统计图')
    @pytest.mark.parametrize('info', yaml.safe_load(
        read_yaml_info(Path.path['INHOS_GLU_PATIENTPIECHART'])))
    def test_patientPieChart(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.PATIENTPIECHART, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.PATIENTPIECHART, info, response,
                                    patientPieChart.PatientPieChart.schema)

    '''
    血糖修改修改时段和血糖值
    '''

    @allure.title('住院患者血糖修改')
    @allure.description('更新血糖，目前写了两个用例，修改时段，修改血糖值')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_UPDATE'])))
    def test_zy_glu_update(self, info):
        if read_yaml('headers')['Platform'] == str(3):

            if info['parame']['deviceNo'] is None:
                info['parame'].pop('deviceNo')
            response = re.request_main('post', Url.GLU_UPDATE, headers=read_yaml('headers'),
                                       json=info['parame'])
        else:
            if info['parame']['deviceNo'] is None:
                info['parame']['deviceNo'] = read_yaml('headers')['sn']
            response = re.request_main('post', Url.GLU_UPDATE, headers=read_yaml('headers'),
                                       json=info['parame'])
        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where id=\'{}\'".format(
                read_bastase_sql()[4],
                info['parame']['id']))
        Encapsulation.repeatThree(Url.GLU_UPDATE, info, response)

        assert data[0]['time_type'] == info['parame']['timeType']
        assert data[0]['value'] == info['parame']['value']
        assert data[0]['comment'] == info['parame']['comment']

        logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_UPDATE)

    @allure.title('住院患者血糖删除')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_DEL'])))
    def test_zy_glu_del(self, info):

        response = re.request_main('post', Url.GLU_DEL, headers=read_yaml('headers'),
                                   json=info['parame'])

        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where id=\'{}\'".format(
                read_bastase_sql()[4],
                info['parame']['id']))
        Encapsulation.repeatThree(Url.GLU_DEL, info, response)

        assert data[0]['status'] == 0
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_DEL)
