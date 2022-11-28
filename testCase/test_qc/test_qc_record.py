import os
import sys
import allure
import pytest
import yaml
from common.read_fun import read_yaml_info
from testCase.log import logger
from common.yaml_util import read_bastase_sql, read_yaml
from common.open_database import MysqlDb
from compare.encapsulation import Encapsulation
from config.contast import Url, Path
from compare import qc, qc_analysis, qc_statistics
from common.http_client import RequestMain
from common.read_fun import LoadBasic
import datetime, time

sys.path.append(r'' + os.path.abspath('../../'))
re = RequestMain()


@allure.feature("质控")
class Test_qc_record(object):
    @allure.title('查询质控')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_LIST'])))
    def test_qc_list(self, info):

        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.QC_LIST, info, response, qc.Qc.get())
                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.PATIENT_LIST, info, response, old_list,
                                                           qc.Qc.get())
                        old_list = new_list

        else:

            if info['version'] == 2 or info['version'] == 1:
                response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])

                Encapsulation.repeatOne(Url.PATIENT_LIST, info, response, qc.Qc.get())
                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.PATIENT_LIST, info, response, old_list,
                                                           qc.Qc.get())
                        old_list = new_list

    @allure.title('编辑质控')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_UPDATE'])))
    def test_qc_update(self, info):

        if read_yaml('headers')['Platform'] == str(3):

            info1 = LoadBasic.read_qc_info()
            if info['parame']['value'] > info1['high'] or info['parame']['value'] < info1['low']:
                info['parame']['result'] = 0
            else:
                info['parame']['result'] = 1

            response = re.request_main('post', Url.QC_UPDATE, headers=read_yaml('headers'),
                                       json=info['parame'])

            data = MysqlDb().select_db(
                "select * from {}.`qc_record` where id =\'{}\'".format(read_bastase_sql()[4], info['parame']['id']))

            data[0]['measure_time'] = data[0]['measure_time'].strftime('%Y-%m-%d %H:%M:%S')
            Encapsulation.repeatThree(Url.QC_UPDATE, info, response)

            assert data[0]['value'] == info['parame']['value']
            assert data[0]['result'] == info['parame']['result']
            assert data[0]['measure_time'] == info['parame']['measureTime']

            logger.log_info.info('---->接口%s结束一次用例测试' % Url.QC_UPDATE)

    @allure.title('删除质控')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_DELETE'])))
    def test_qc_delete(self, info):

        response = re.request_main('post', Url.QC_DELETE, headers=read_yaml('headers'),
                                   json=info['parame'])

        data = MysqlDb().select_db(
            "select * from {}.`qc_record` where id =\'{}\'".format(read_bastase_sql()[4], info['parame']['id']))

        Encapsulation.repeatThree(Url.QC_DELETE, info, response)
        assert data[0]['status'] == 0
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.QC_DELETE)

    #
    @allure.title('添加质控')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_ADD'])))
    def test_qc_add(self, info):

        response = re.request_main('post', Url.QC_ADD, headers=read_yaml('headers'),
                                   json=info['parame'])

        data = MysqlDb().select_db(
            "select * from {}.`qc_record` order by id desc".format(read_bastase_sql()[4]))

        Encapsulation.repeatThree(Url.QC_ADD, info, response)
        assert data[0]['value'] == info['parame']['value']
        assert data[0]['result'] == info['parame']['result']

        logger.log_info.info('---->接口%s结束一次用例测试' % Url.QC_ADD)

    #
    @allure.title('质控分析')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_ANALYSIS'])))
    def test_qc_analysis(self, info):

        if read_yaml('headers')['Platform'] == str(3):
            now = datetime.date.today()
            info['parame']['measureTimeStart'] = datetime.datetime(now.year, now.month, 1).strftime('%Y-%m-%d 00:00:00')
            info['parame']['measureTimeEnd'] = time.strftime("%Y-%m-%d 23:59:59", time.localtime())

            response = re.request_main('post', Url.QC_ANALYSIS, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.QC_ANALYSIS, info, response, qc_analysis.Analysis.schema)

    #
    @allure.title('质控统计')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['QC_RECORD_STATISTICS'])))
    def test_qc_statistics(self, info):

        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.QC_STATISTICS, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.QC_STATISTICS, info, response, qc_statistics.QcStatistic.get())
