# coding=UTF-8
import os
import sys
import ru

import shutil,pytest

sys.path.append(r'' + os.path.abspath('../'))

if __name__ == '__main__':
    try:
        shutil.rmtree('../result')
        shutil.rmtree('../report_allure')
    except:
        pass
    ru.clear()
    ru.login()
    # pytest.main(["-sv", './test_zhuyuan/test_patient.py'])
    # pytest.main(["-spatient_v", './test_zhuyuan/test_patient_blood.py'])
    # pytest.main(["-sv", './test_zhuyuan/test_temp_blood.py'])
    # for i in Path.path['basic'].values():
    #     clear_yaml(i)

    # login()
    # if '101' in read_yaml('permissions'):
    #     response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
    #                                json=A.zy().get_patient_info())
    #     if response['data']['count'] != 0:
    #         info = re.request_main('post', Url.PATIENT_INFO, headers=read_yaml('headers'),
    #                                json={"userId": response['data']['lists'][0]['userId']})
    #         write_yaml(info['data'], Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])
    #         userid = info['data']['userId']
    #         response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
    #                                    json=A.zy().get_blood_info(userid))
    #     pytest.main(["-sv", './test_zhuyuan/test_patient.py'])

    #         if response['data']['count'] == 0:
    #             response = requests.post(Url.GLU_ADD, headers=read_yaml('headers'),
    #                                      data=A.zy().add_glu(userid)).json()
    #             response = requests.post(Url.GLU_LIST, headers=read_yaml('headers'),
    #                                      data=A.zy().get_blood_info(userid)).json()
    #         write_yaml(response['data']['lists'][0], Path.path['basic']['inhos_patient_blood_info'])
    #         pytest.main(["-sv", './test_zhuyuan/test_patient_blood.py::Test_zy_blood::test_zy_glu_update'])
    #         #         # write_yaml({'patient_blood': info['data']}, load(Path)['basic']['header_path'])
    #         # pytest.main(["-sv", './test_zhuyuan/test_temp_blood.py::Test_temp_blood::test_add_temp_blood'])


        # pytest.main(["-sv", './test_common/test_common.py', '--alluredir', '../result'])

#     #     info = requests.post(url.format('inhos/measure/glu_order/web_monitorList'), headers=read_yaml('headers'),
#     #                          data=A.zy().get_order()).json()
#     #
#     #     if info['data']['count'] == 0:
#     #         respon = requests.post(url.format('inhos/measure/glu_order/add'),
#     #                                headers=read_yaml('headers'),
#     #                                data=A.zy().add_order(userid)).json()
#     #     response1 = requests.post(url.format('inhos/measure/glu_order/web_monitorList'), headers=read_yaml('headers'),
#     #                               data=A.zy().get_order()).json()
#     #
#     #     id = response1['data']['lists'][0]['id']
#     #     data = MysqlDb().select_db(
#     #         "select * from {}.`medical_order_detail`where id=\'{}\' ".format(read_bastase_sql()[4],
#     #                                                                          id))
#     #
#     #     if response1['data']['analysisModel'] == 0:
#     #         write_yaml({'analysisModel': response1['data']['analysisModel']}, load(Path)['basic']['order_info'])
#     #         write_yaml(response1['data']['lists'][0], load(Path)['basic']['order_info'])
#     #         write_yaml({'orderid': data[0]['order_id']}, load(Path)['basic']['order_info'])
#     #     if response1['data']['analysisModel'] == 1:
#     #         write_yaml({'analysisModel': response1['data']['analysisModel']}, load(Path)['basic']['order_info'])
#     #         for i in response1['data']['lists']:
#     #             i['status'] = 1
#     #             write_yaml(i, load(Path)['basic']['order_info'])
#     #             write_yaml({'orderid': data[0]['order_id']}, load(Path)['basic']['order_info'])
#     #             break
#     #     pytest.main(["-sv", './test_zhuyuan/test_order.py', '--alluredir', '../result'])
#     #     # pytest.main(["-sv", './test_zhuyuan/test_order.py'])
#     #
#     #     response = requests.post(url.format('inhos/measure/temp/list'), headers=read_yaml('headers'),
#     #                              data=A.zy_temp().tmep_glu_list()).json()
#     #     if response['data']['count'] == 0:
#     #         response = requests.post(url.format('inhos/measure/temp/add'), headers=read_yaml('headers'),
#     #                                  data=A.zy_temp().add_glu()).json()
#     #
#     #     response1 = requests.post(url.format('inhos/measure/temp/list'), headers=read_yaml('headers'),
#     #                               data=A.zy_temp().tmep_glu_list()
#     #                               ).json()
#     #     write_yaml(response1['data']['lists'][0], load(Path)['basic']['inhos_temp_info'])
#     #     # pytest.main(["-sv", './test_zhuyuan/test_temp_blood.py', '--alluredir', '../result'])
#     #
#     # paper = requests.post(url.format('paper/list'), headers=read_yaml('headers'),
#     #                       data=json.dumps({}),timeout=60).json()
#     #
#     # liquid = requests.post(url.format('qc/liquid/list'), headers=read_yaml('headers'),
#     #                        data=json.dumps({}),timeout=60).json()
#     #
#     # sn = requests.post(url.format('device/list'), headers=read_yaml('headers'),
#     #                    data=json.dumps({"pageNo": -1, 'pageSize': 10}),timeout=60).json()
#     # l1=[]
#     # l2=[]
#     # l3=[]
#     # for i in sn['data']['lists']:
#     #     if i['devStatus'] == 0:
#     #         l1.append(i)
#     #
#     # for i in liquid['data']['lists']:
#     #     b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
#     #     if b >= datetime.datetime.now():
#     #         l2.append(i)
#     #         # break
#     #
#     # for i in paper['data']['lists']:
#     #     b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
#     #     if b >= datetime.datetime.now():
#     #         l3.append(i)
#     #         # break
#     #
#     # write_yaml(l3, load(Path)['basic']['paper_info'])
#     # write_yaml(l2, load(Path)['basic']['liquid_info'])
#     # write_yaml(l1, load(Path)['basic']['sn_info'])
#     #
#     # if '10601' in read_yaml('permissions'):
#     #     response = requests.post(url.format('qc/record/list'), headers=read_yaml('headers'),
#     #                              data=json.dumps({"pageNo": 1, 'pageSize': 15})).json()
#     #     if response['data']['count'] == 0:
#     #         response = requests.post(url.format('qc/record/add'), headers=read_yaml('headers'),
#     #                                  data=json.dumps(A.qc_record().qc_add())).json()
#     #     response = requests.post(url.format('qc/record/list'), headers=read_yaml('headers'),
#     #                              data=json.dumps({"pageNo": 1, 'pageSize': 15})).json()
#     #     write_yaml(response['data']['lists'][0], load(Path)['basic']['qc_info'])
#     #
#     #     # pytest.main(["-sv", './test_qc/test_qc_record.py::Test_qc_record::test_qc_add'])
#     #     # pytest.main(["-sv", './test_qc/test_qc_record.py', '--alluredir', '../result'])
#     #
#     # if '102' in read_yaml('permissions'):
#     #     response = requests.post(url.format('mz/patient/list'), headers=read_yaml('headers'),
#     #                              data=A.mz().get_patient_info()).json()
#     #     if response['data']['count'] != 0:
#     #         info = requests.post(url.format('mz/patient/info'), headers=read_yaml('headers'),
#     #                              data=json.dumps({"userId": response['data']['lists'][0]['userId']})).json()
#     #
#     #         userId = response['data']['lists'][0]['userId']
#     #         write_yaml(info['data'], load(Path)['basic']['mz_patient_info'])
#     #         response = requests.post(url.format('mz/glu/list'), headers=read_yaml('headers'),
#     #                                  data=A.mz().get_blood_info(userId)).json()
#     #         if response['data']['count'] == 0:
#     #             requests.post(url.format('mz/glu/add'), headers=read_yaml('headers'),
#     #                           data=A.mz().add_glu(userId)).json()
#     #             response = requests.post(url.format('mz/glu/list'), headers=read_yaml('headers'),
#     #                                      data=A.mz().get_blood_info(userId)).json()
#     #
#     #         write_yaml(response['data']['lists'][0], load(Path)['basic']['mz_patient_blood_info'])
#     #     # print(response1['data']['lists'])
#     #     #     write_yaml(sn['data']['lists'], load(Path)['basic']['sn_info'])
#     #
