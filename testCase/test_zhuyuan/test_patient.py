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
from compare import patient, leavePatient, patientInfo, healthArchives
from common.httpClient import RequestMain
from datetime import datetime

sys.path.append(r'' + os.path.abspath('../../'))
re = RequestMain()


@allure.feature('住院患者')
class TestZhuYuan(object):
    @allure.title('患者列表')
    @pytest.mark.skipif('201010101' not in read_yaml('permissions') and "1010101" not in read_yaml('permissions'),
                        reason='该账号无此权限')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['INHOS_PATIENT_LIST'])))
    def test_in_patient(self, info):
        if read_yaml('headers')['Platform'] == "3":
            if info['version'] == 2 or info['version'] == 3:
                response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.PATIENT_LIST, info, response, patient.Patinet.get())
                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.PATIENT_LIST, info, response, old_list,
                                                           patient.Patinet.get())
                        old_list = new_list

        else:
            if info['version'] == 2 or info['version'] == str(1):
                response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                           json=info['parame'])
                Encapsulation.repeatOne(Url.PATIENT_LIST, info, response, patient.Patinet.get())
                if response['data']['totalPage'] > 1:
                    old_list = response['data']['lists']
                    for i in range(2, response['data']['totalPage'] + 1):
                        info['parame']['pageNo'] = i
                        response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
                                                   json=info['parame'])
                        new_list = Encapsulation.repeatTwo(Url.PATIENT_LIST, info, response, old_list,
                                                           patient.Patinet.get())
                        old_list = new_list

    @allure.title('出院患者列表')
    @pytest.mark.skipif('1010102' not in read_yaml('permissions'), reason='该账号无此权限')
    @pytest.mark.dependency(name='test_out_patient')
    @allure.description('该接口写了4个用例包含所有出院患者，根据科室筛选，根据住院号,根据姓名筛选')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['INHOS_PATIENT_LIST_LEAVE'])))
    def test_out_patient(self, info):
        if read_yaml('headers')['Platform'] == '3':
            response = re.request_main('post', Url.PATIENT_LEAVE, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.PATIENT_LEAVE, info, response,
                                    leavePatient.leavePatinet.get())
            if response['data']['totalPage'] > 1:
                old_list = response['data']['lists']
                for i in range(2, response['data']['totalPage'] + 1):
                    info['parame']['pageNo'] = i
                    response = re.request_main('post', Url.PATIENT_LEAVE, headers=read_yaml('headers'),
                                               json=info['parame'])
                    new_list = Encapsulation.repeatTwo(Url.PATIENT_LEAVE, info, response, old_list,
                                                       leavePatient.leavePatinet.get())
                    old_list = new_list
                    if i == 5:
                        break

    @allure.title('出院患者入院')
    @pytest.mark.skipif('1010102010101' not in read_yaml('permissions'), reason='该账号无此权限')
    @pytest.mark.dependency(depends=["test_out_patient"])
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['OUT_PATIENT_ADD_IPT'])))
    @allure.description('出院患者入院')
    def test_out_patient_add_ipt(self, info):

        response = re.request_main('post', Url.PATIENT_LEAVE, headers=read_yaml('headers'),
                                   json={"pageNo": 1, "pageSize": 15})
        if response['data']['count'] != 0:
            out_patient_info = response['data']['lists'][0]
            info['parame']['name'] = out_patient_info['name']
            info['parame']['gender'] = out_patient_info['gender']
            birthday = datetime.strptime(out_patient_info['birthday'], '%Y-%m-%d %H:%M:%S')
            birthday = birthday.strftime('%Y-%m-%d')
            info['parame']['birthday'] = birthday
            info['parame']['userId'] = out_patient_info['userId']
            info['parame']['deptId'] = out_patient_info['deptId']
            info['parame']['deptName'] = out_patient_info['deptName']

            if info['parame']['iptNum'] is None:
                info['parame']['iptNum'] = out_patient_info['iptNum']

            response = re.request_main('post', Url.PATIENT_ADDIPT, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatThree(Url.PATIENT_ADDIPT, info, response)
            if response['code'] == 0:
                data = MysqlDb().select_db(
                    "select * from {}.`patient_info`where user_id=\'{}\'".format(read_bastase_sql()[4],
                                                                                 info['parame'][
                                                                                     'userId']))

                assert data[0]['status'] == 1


            logger.log_info.info('---->接口%s结束一次用例测试' % Url.PATIENT_ADDIPT)


        else:
            logger.log_info.info('没有出院患者')

    @allure.title('患者详情')
    @pytest.mark.skipif('101010102' not in read_yaml('permissions') and "201010102" not in read_yaml('permissions'),
                        reason='该账号无此权限')
    @allure.description('该接口写了2个用例根据userid或者住院号')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['INHOS_PATIENT_INFO'])))
    def test_patient_info(self, info):
        response = re.request_main('post', Url.PATIENT_INFO, headers=read_yaml('headers'),
                                   json=info['parame'])
        Encapsulation.repeatOne(Url.PATIENT_INFO, info, response, patientInfo.PatientInfo.schema)

    #
    @allure.title('控糖目标')
    @pytest.mark.skipif('101010102' not in read_yaml('permissions') and "201010102" not in read_yaml('permissions'),
                        reason='该账号无此权限')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(
                                 read_yaml_info(Path.path['INHOS_PATIENT_INFO_HEALTHARCHIVES'])))
    def test_healthArchives(self, info):
        if read_yaml('headers')['Platform'] == '3':
            response = re.request_main('post', Url.HEALTH_ARCHIVES, headers=read_yaml('headers'),
                                       json=info['parame'])

            Encapsulation.repeatOne(Url.HEALTH_ARCHIVES, info, response,
                                    healthArchives.healthArchives.schema)


    @allure.title('换床')
    @pytest.mark.skipif('1010101020104' not in read_yaml('permissions'),
                        reason='该账号无此权限')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['INHOS_PATIENT_CHANGEBED'])))
    def test_change_bed(self, info):
        if read_yaml('headers')['Platform'] == str(3):
            response = re.request_main('post', Url.CHANGE_BED, headers=read_yaml('headers'),
                                       json=info['parame'])

            data = MysqlDb().select_db(
                "select * from {}.`patient_info`where user_id=\'{}\'".format(read_bastase_sql()[4],
                                                                             info['parame'][
                                                                                 'userId']))

            Encapsulation.repeatThree(Url.CHANGE_BED, info, response)
            assert eval(data[0]['bed_num']) == info['parame']['bedNum']

            logger.log_info.info('---->接口%s结束一次用例测试' % Url.CHANGE_BED)

        '''
        # 更新患者信息，2个用例，修改手机号，修改床号
        # '''

    @allure.title('更新患者基本信息')
    @pytest.mark.skipif('1010101020301' not in read_yaml('permissions'),
                        reason='该账号无此权限')
    @allure.description('更新患者信息，2个用例必传，修改手机号，修改床号')
    @pytest.mark.parametrize('info',
                             yaml.safe_load(read_yaml_info(Path.path['INHOS_PATIENT_UPDATE'])))
    def test_update_patient_info(self, info):
        info['parame']['birthday'] = info['parame']['birthday'].strftime('%Y-%m-%d')

        response = re.request_main('post', Url.PATIENT_UPDATE, headers=read_yaml('headers'),
                                   json=info['parame'])
        data = MysqlDb().select_db("select * from {}.`patient_info`where user_id=\'{}\'".format(read_bastase_sql()[4],
                                                                                                info['parame'][
                                                                                                    'userId']))
        Encapsulation.repeatThree(Url.PATIENT_UPDATE, info, response)

        assert data[0]['bed_num'] == info['parame']['bedNum']
        assert data[0]['phone'] == info['parame']['phone']
        logger.log_info.info('---->接口%s结束一次用例测试' % Url.PATIENT_UPDATE)

    # @allure.title('患者出院')
    # @pytest.mark.parametrize('info', [
    #     zy().out_hospital()])
    # def test_out_hospital(self, info):
    #
    #     response = re.request_main(url.format('inhos/patient/outHospital'), headers=read_yaml('headers'),
    #                              data=info).json()
    #     logger.getlogger().info('出院患者：请求头%s传参%s返回体%s',
    #                             read_yaml('headers'), info, response)
    #
    #     data = MysqlDb().select_db("select * from {}.`patient_info`where user_id=\'{}\'".format(read_bastase_sql()[4],
    #
    #                                                                                             read_zy_yaml()[
    #                                                                                                 'userId']))
    #     try:
    #         assert data[0]['status'] == 0
    #         assert response['code'] == 0
    #         assert response['msg'] == '请求成功'
    #     except AssertionError:
    #         logger.getlogger().error("出院患者 %s", "接口报错", exc_info=1)
    #         assert response['code'] == 0
    #         assert data[0]['status'] == 0

    # @allure.title('添加患者')
    # @pytest.mark.skipif('101010101' not in read_yaml('permissions'),
    #                     reason='该账号无此权限')
    # @pytest.mark.parametrize('info',
    #                          yaml.safe_load(read_yaml_info(Path.path['inhos_patient_add'])))
    # def test_add_patient(self, info):
    #     response = re.request_main('post', Url.PATIENT_ADD, headers=read_yaml('headers'),
    #                                json=info['parame'])
    #     data = MysqlDb().select_db(
    #         "select * from {}.`patient_info` ORDER BY id desc limit 1".format(read_bastase_sql()[4]))
    #     if response["msg"] == '住院号或身份证已经被绑定':
    #         logger.log_info.info("检查住院号或身份证号是否被绑定")
    #
    #     else:
    #         Encapsulation.repeatThree(Url.PATIENT_ADD, info, response)
    #         assert data[0]['ipt_num'] == info['parame']['iptNum']
    #         logger.log_info.info('---->接口%s结束一次用例测试' % Url.PATIENT_ADD)
