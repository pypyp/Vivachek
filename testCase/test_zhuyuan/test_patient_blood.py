# coding=UTF-8
import os
import sys

import allure
import pytest
import yaml

from common.http_client import RequestMain
from common.open_database import MysqlDb
from common.read_fun import read_yaml_info
from common.yaml_util import read_yaml
from compare import glu_list, glu_info, patient_trend_chart, patient_pie_chart, measure, \
    app_report
from compare.encapsulation import Encapsulation
from config.contast import Url, Path, Config
from testCase.log import logger

sys.path.append(r'' + os.path.abspath('../../'))

re = RequestMain()


@allure.feature("住院患者血糖")
class Test_zy_blood(object):
    @allure.title('住院患者血糖列表')
    @pytest.mark.skipif(
        '1010101020202' not in read_yaml('permissions') and "2010101020204" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @allure.description('该接口写了4个用例,全部血糖和按时间查询')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_LIST'])))
    def test_zy_glu_list(self, info):

        if read_yaml('headers')['Platform'] == '3':
            if info['version'] == 2 or info['version'] == 3:

                response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.GLU_LIST, info, response, glu_list.GluList.get())

                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.GLU_LIST, info, response, old_list,
                                                           glu_list.GluList.get())
                        old_list = new_list

        elif read_yaml('headers')['Platform'] == '1':

            if info['version'] == 2 or info['version'] == 1:

                response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.GLU_LIST, info, response, glu_list.GluList.get())

                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.GLU_LIST, info, response, old_list,
                                                           glu_list.GluList.get())
                        old_list = new_list

    @allure.title('住院患者血糖报告')
    @pytest.mark.skipif(
        '1010101020201' not in read_yaml('permissions') and "2010101020203" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @allure.description('该接口写了4个用例,全部血糖和按时间查询')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_REPORT'])))
    def test_zy_glu_report(self, info):
        if read_yaml('headers')['Platform'] == '3':
            if info['version'] == 2 or info['version'] == 3:

                response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_REPORT, info, response, glu_list.GluList.get())

                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.GLU_REPORT, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.GLU_REPORT, info, response, old_list,
                                                           glu_list.GluList.get())
                        old_list = new_list
        #
        elif read_yaml('headers')['Platform'] == '1':
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.GLU_APP_REPORT, headers=read_yaml('headers'),
                                           json=info['parame'])
                if len(response['data']) == 0:
                    logger.log_info.info('没有血糖数据')
                else:
                    DICT = {"type": "array", }
                    report = app_report.AppGluReport.get()
                    item = report.AppGluReport.item
                    DICT['items'] = item
                    L = []
                    for i in response['data']:
                        for j in i.keys():
                            L.append(j)
                    L = list(set(L))
                    L.remove('date')

                    for i in L:
                        report["data"]["items"]["properties"][i] = DICT

                    Encapsulation.repeatOne(Url.GLU_APP_REPORT, info, response, app_report)

    @pytest.mark.skipif(
        '10101010202' not in read_yaml('permissions') and "20102" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_MEASURE_GLU'])))
    def test_zy_measure_glu(self, info):
        if read_yaml('headers')['Platform'] == '3':
            if info['version'] == 2 or info['version'] == 3:

                response = re.request_main('post', Url.GLU_WEB_MEASURE, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.GLU_WEB_MEASURE, info, response, glu_list.GluList.get())

                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.GLU_WEB_MEASURE, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.GLU_WEB_MEASURE, info, response, old_list,
                                                           glu_list.GluList.get())
                        old_list = new_list
        #
        elif read_yaml('headers')['Platform'] == '1':
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.GLU_APP_MEASURE, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.GLU_APP_REPORT, info, response, measure.Measure.get())

    @allure.title('住院血糖详情')
    @pytest.mark.skipif(
        '10101010202' not in read_yaml('permissions'), reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_INFO'])))
    def test_glu_info(self, info):
        if read_yaml('headers')['Platform'] == '3':
            response = re.request_main('post', Url.GLU_INFO, headers=read_yaml('headers'),
                                       json=info['parame'])
            Encapsulation.repeatOne(Url.GLU_INFO, info, response, glu_info.GluInfo.schema)

    @allure.title('住院血糖添加')
    @pytest.mark.skipif(
        '1010101020102' not in read_yaml('permissions') and "2010101020201" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_ADD'])))
    @allure.description('该接口写了10个用例，正常血糖，25.5，0.6，以及各种状态')
    def test_add_zy_blood(self, info):
        if read_yaml('headers')['Platform'] == '3':
            response = re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
                                       json=info['parame'])
        else:
            info['parame']['deviceNo'] = read_yaml('headers')['sn']
            info['parame']['method'] = 1

            response = re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
                                       json=info['parame'])
        Encapsulation.repeatThree(Url.GLU_ADD, info, response)

        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where  user_id=\'{}\' ORDER BY id DESC limit 1".format(
                Config.database['database'],
                info['parame']['userId']
            ))
        try:
            info['parame']['comment']
        except:
            info['parame']['comment'] = None

        assert str(data[0]['measure_time']) == info['parame']['measureTime']
        assert data[0]['comment'] == info['parame']['comment']
        assert data[0]['unusual'] == info['parame']['unusual']
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_ADD)

    @allure.title('住院患者血糖趋势图')
    @pytest.mark.skipif(
        '1010101020203' not in read_yaml('permissions') and "2010101020205" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(
        read_yaml_info(Path.path['INHOS_GLU_PATIENTTRENDCHART'])))
    def test_patientTrendChart(self, info):
        if read_yaml('headers')['Platform'] == '3':
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.PATIENTTRENDCHART, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.PATIENTTRENDCHART, info, response,
                                        patient_trend_chart.PatientTrendChart.schema)
        elif read_yaml('headers')['Platform'] == '1':
            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.PATIENTTRENDCHART, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.PATIENTTRENDCHART, info, response,
                                        patient_trend_chart.PatientTrendChart.schema)

    @allure.title('住院患者血糖统计图')
    @pytest.mark.skipif(
        '1010101020204' not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(
        read_yaml_info(Path.path['INHOS_GLU_PATIENTPIECHART'])))
    def test_patientPieChart(self, info):
        if read_yaml('headers')['Platform'] == '3':
            response = re.request_main('post', Url.PATIENTPIECHART, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.PATIENTPIECHART, info, response,
                                    patient_pie_chart.PatientPieChart.schema)

    @allure.title('住院患者血糖修改')
    @pytest.mark.skipif(
        '1010101020208' not in read_yaml('permissions') and "2010101020202" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @allure.description('更新血糖，目前写了两个用例，修改时段，修改血糖值')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_UPDATE'])))
    def test_zy_glu_update(self, info):
        if read_yaml('headers')['Platform'] == '3':

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
                Config.database['database'],
                info['parame']['id']))
        Encapsulation.repeatThree(Url.GLU_UPDATE, info, response)

        assert data[0]['time_type'] == info['parame']['timeType']
        assert data[0]['value'] == info['parame']['value']
        assert data[0]['comment'] == info['parame']['comment']

        logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_UPDATE)

    #
    @allure.title('住院患者血糖删除')
    @pytest.mark.skipif(
        '1010101020208' not in read_yaml('permissions') and "2010101020202" not in read_yaml('permissions'),
        reason='该账号无此权限')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_GLU_DEL'])))
    def test_zy_glu_del(self, info):

        response = re.request_main('post', Url.GLU_DEL, headers=read_yaml('headers'),
                                   json=info['parame'])

        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where id=\'{}\'".format(
                Config.database['database'],
                info['parame']['id']))
        Encapsulation.repeatThree(Url.GLU_DEL, info, response)

        assert data[0]['status'] == 0
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.GLU_DEL)
