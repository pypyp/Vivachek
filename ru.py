# coding=UTF-8
# import os
import os
import sys
from testCase.log import logger

from config.contast import Url, Header, Client_Header,Config
from common.http_client import RequestMain

sys.path.append(r'' + os.path.abspath('/'))
re = RequestMain()

class BasicConfiguration(object):



    """
    登陆账号获取token已经账号的数据权限
    """
    @staticmethod
    def login():
        BasicConfiguration.clear()
        result = BasicConfiguration.check_is_open(Config.IP, int(Config.PORT))
        if result is True:
            global header
            info = Config.info

            type = info['type']
            if type == 1:
                info['login']['sn'] = Client_Header.header['sn']
                header = Client_Header.header
                order = Url.APP_MONITORLIST
                paper_url = Url.PAPER + '/number'
                liquild_url = Url.LIQUID + '/number'
            elif type == 3:
                header = Header.header
                order = Url.WEB_MONITORLIST
                paper_url = Url.PAPER
                liquild_url = Url.LIQUID

            logger.log_info.info("登陆,获取token以及账号的一些基础信息")

            response = re.request_main('post', Url.LOGIN, headers=header, json=info['login'])



            # header["Access-Token"] = response['data']['accessToken']
            # header["refresh_token"] = response['data']['refreshToken']
            # write_yaml({'headers': header}, Path.path['basic']['HEADER_PATH'])
            # write_yaml({"userId": response['data']["userId"]}, Path.path['basic']['HEADER_PATH'])
            #
            # if info['login']['hisId'] == 'vivachek':
            #     dept = re.request_main('post', Url.DEPT, headers=read_yaml('headers'),
            #                            json={"inhos": 1})
            #     l = []
            #     for i in dept['data']:
            #         l.append(i['id'])
            #     write_yaml({"deptId": l[0]}, Path.path['basic']['HEADER_PATH'])
            #     write_yaml({"auth": l}, Path.path['basic']['HEADER_PATH'])
            # write_yaml({"deptId": response['data']['deptId']}, Path.path['basic']['HEADER_PATH'])
            # write_yaml({"auth": response['data']['dataAuthIds']}, Path.path['basic']['HEADER_PATH'])
            # write_yaml({"hosId": response['data']["hosId"]}, Path.path['basic']['HEADER_PATH'])
            # info = response['data']["permissions"]
            # l = []
            # for i in info:
            #     l.append(i['id'])
            # write_yaml({"permissions": l}, Path.path['basic']['HEADER_PATH'])
            # logger.log_info.info("登陆完成")
#     logger.log_info.info("根据配置加载患者、血糖、质控等基础信息")
#     if '101' or '201' in read_yaml('permissions'):
#         response = re.request_main('post', Url.PATIENT_LIST, headers=read_yaml('headers'),
#                                    json=zy.get_patient_info())
#         if response['data']['count'] != 0:
#             info = re.request_main('post', Url.PATIENT_INFO, headers=read_yaml('headers'),
#                                    json={"userId": response['data']['lists'][0]['userId']})
#             write_yaml(info['data'], Path.path['basic']['INHOS_PATIENT_BASIC_INFO'])
#             userid = info['data']['userId']
#             response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
#                                        json=zy.get_blood_info(userid))
#         if response['data']['count'] == 0:
#             re.request_main('post', Url.GLU_ADD, headers=read_yaml('headers'),
#                             json=zy.add_glu(userid))
#             response = re.request_main('post', Url.GLU_LIST, headers=read_yaml('headers'),
#                                        json=zy.get_blood_info(userid))
#         write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_PATIENT_BLOOD_INFO'])
#
#         response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
#                                    json=zy_temp.tmep_glu_list())
#
#         if response['data']['count'] == 0:
#             re.request_main('post', Url.TEMP_ADD, headers=read_yaml('headers'),
#                             json=zy_temp.add_glu())
#
#         response = re.request_main('post', Url.TEMP_LIST, headers=read_yaml('headers'),
#                                    json=zy_temp.tmep_glu_list())
#
#         write_yaml(response['data']['lists'][0], Path.path['basic']['INHOS_TEMP_INFO'])
#
#         response = re.request_main('post', order, headers=read_yaml('headers'),
#                                    json=zy.get_order())
#         write_yaml({'analysisModel': response['data']['analysisModel']}, Path.path['basic']['ORDER_INFO'])
#         if order == Url.WEB_MONITORLIST:
#             id = response['data']['lists'][0]['id']
#             data = MysqlDb().select_db(
#                 "select * from {}.`medical_order_detail`where id=\'{}\' ".format(read_bastase_sql()[4],
#                                                                                  id))
#             if response['data']['analysisModel'] == 0:
#                 write_yaml(response['data']['lists'][0], Path.path['basic']['ORDER_INFO'])
#                 write_yaml({'orderid': data[0]['order_id']}, Path.path['basic']['ORDER_INFO'])
#             if response['data']['analysisModel'] == 1:
#                 for i in response['data']['lists']:
#                     if i['status'] == 1:
#                         write_yaml(i, Path.path['basic']['ORDER_INFO'])
#                         write_yaml({'orderid': data[0]['order_id']}, Path.path['basic']['ORDER_INFO'])
#                         break
#         else:
#             if "tasks" in response['data'].keys():
#                 write_yaml(response['data']['tasks'][0], Path.path['basic']['ORDER_INFO'])
#             else:
#                 write_yaml(response['data']['taskLookupList'][0]['tasks'][0], Path.path['basic']['ORDER_INFO'])
#
#     if '105' or '205' in read_yaml('permissions'):
#         paper = re.request_main('post', paper_url, headers=read_yaml('headers'),
#                                 json={})
#
#         liquid = re.request_main('post', liquild_url, headers=read_yaml('headers'),
#                                  json={})
#
#         sn = re.request_main('post', Url.SN, headers=read_yaml('headers'),
#                              json={"pageNo": -1, 'pageSize': 10})
#
#         l1 = []
#         l2 = []
#         l3 = []
#         try:
#             liquid_info = liquid['data']['lists']
#             paper_info = paper['data']['lists']
#         except:
#             liquid_info = liquid['data']
#             paper_info = paper['data']
#         for i in sn['data']['lists']:
#             if i['devStatus'] == 0:
#                 l1.append(i)
#
#         for i in liquid_info:
#             b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
#             if b >= datetime.datetime.now():
#                 l2.append(i)
#                 # break
#
#         for i in paper_info:
#             b = datetime.datetime(*map(int, i['expiryDate'].split('-')))
#             if b >= datetime.datetime.now():
#                 l3.append(i)
#                 # break
#
#         write_yaml(l3, Path.path['basic']['PAPER_INFO'])
#         write_yaml(l2, Path.path['basic']['LIQUID_INFO'])
#         write_yaml(l1, Path.path['basic']['SN_INFO'])
#     response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
#                                json={"pageNo": 1, 'pageSize': 15})
#     if response['data']['count'] == 0:
#         re.request_main('post', Url.QC_ADD, headers=read_yaml('headers'),
#                         json=qc_record.qc_add())
#     response = re.request_main('post', Url.QC_LIST, headers=read_yaml('headers'),
#                                json={"pageNo": 1, 'pageSize': 15})
#     write_yaml(response['data']['lists'][0], Path.path['basic']['QC_INFO'])
#
#
# logger.log_info.info("信息加载完成")

