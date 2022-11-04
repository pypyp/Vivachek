# coding=UTF-8
import os
import sys
import pytest
import allure
from common.yaml_util import read_yaml, read_url_csv, read_bastase_sql
from common.read_fun import read_yaml_info
from testCase.log import logger
import  yaml
from common.open_database import MysqlDb
from config.contast import Url, Path
from compare.encapsulation import Encapsulation
from compare import tempBlood
from common.httpClient import RequestMain

sys.path.append(r'' + os.path.abspath('../../'))
re = RequestMain()


@allure.feature("临时检测血糖")
class Test_temp_blood(object):
    '''
    2条用例,一条没有关联患者，一条关联患者
    '''

    @allure.title('临时检测血糖添加')
    @allure.description('该接口写了2个用例添加临时检测，添加时绑定患者')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_MEASURE_TEMP_ADD'])))
    def test_add_temp_blood(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == str(2) or info['version'] == str(3):
                response = re.request_main('post', Url.TEMP_ADD, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatThree(Url.TEMP_ADD, info, response)
                data = MysqlDb().select_db(
                    "select * from {}.`blood_glucose_record` order by id desc limit 1".format(
                        read_bastase_sql()[4]
                    ))
                data[0]['measure_time'] = data[0]['measure_time'].strftime('%Y-%m-%d %H:%M:%S')

                assert data[0]['value'] == info['parame']['value']
                assert data[0]['measure_time'] == info['parame']['measureTime']
                logger.log_info.info('---->接口%s结束一次用例测试' % Url.TEMP_ADD)
        elif read_yaml('headers')['Platform'] == str(1):
            if info['version'] == str(1) or info['version'] == str(3):
                response = re.request_main('post', Url.TEMP_ADD, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatThree(Url.TEMP_ADD, info, response)
                data = MysqlDb().select_db(
                    "select * from {}.`blood_glucose_record` order by id desc limit 1".format(
                        read_bastase_sql()[4]
                    ))
                data[0]['measure_time'] = data[0]['measure_time'].strftime('%Y-%m-%d %H:%M:%S')

                assert data[0]['value'] == info['parame']['value']
                assert data[0]['measure_time'] == info['parame']['measureTime']
                logger.log_info.info('---->接口%s结束一次用例测试' % Url.TEMP_ADD)

    @allure.title('临时检测血糖列表')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_MEASURE_TEMP_LIST'])))
    def test_temp_glu_list(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.TEMP_LIST, info, response, tempBlood.TempBlood.schema)
        elif read_yaml('headers')['Platform'] == 1:
            if info['version'] == 2 or info['version'] == str(1):
                response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.TEMP_LIST, info, response, tempBlood.TempBlood.schema)

    @allure.title('临时检测血糖修改')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_MEASURE_TEMP_UPDATE'])))
    def test_temp_glu_update(self, info):
        response = re.request_main('post',Url.TEMP_UPDATE, headers=read_yaml('headers'),
                                 json=info['parame'])
        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where id=\'{}\'".format(
                read_bastase_sql()[4],
                info['parame']['id'],

            ))
        Encapsulation.repeatThree(Url.TEMP_UPDATE, info, response)

        assert data[0]['time_type'] == info['parame']['timeType']

        logger.log_info.info('---->接口%s结束一次用例测试' % Url.TEMP_UPDATE)

    @allure.title('临时检测血糖删除')
    @pytest.mark.parametrize('info', yaml.safe_load(read_yaml_info(Path.path['INHOS_MEASURE_TEMP_DELETE'])))
    def test_temp_glu_del(self, info):

        response = re.request_main('post', Url.TEMP_DEL, headers=read_yaml('headers'),
                                   json=info['parame'])
        data = MysqlDb().select_db(
            "select * from {}.`blood_glucose_record` where id=\'{}\'".format(
                read_bastase_sql()[4],
                info['parame']['id'],

            ))
        Encapsulation.repeatThree(Url.TEMP_UPDATE, info, response)

        assert data[0]['status'] == 0
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.TEMP_DEL)

