# import pytest
# import requests
# from common.yaml_util import clear_yaml,write_yaml,read_yaml,clear_menzhen_yaml,read_url_csv
# from data import menzhen
# from testCase.log import logger
# url = read_url_csv()[0]
#
# from common.yaml_util import read_csv
#
#
# @pytest.fixture(scope='function')
# def login():
#     try:
#         response = requests.post(url.format('login'), headers=menzhen.getheader(), data=menzhen.login(read_csv()[0],
#                                                                                                       read_csv()[1]))
#     except:
#         logger.getlogger().error("登陆报错检测是不是服务没起，还是账号密码错误")
#
#     headers = menzhen.getheader()
#
#     headers["Access-Token"] = response.json()['data']['accessToken']
#     headers["refresh_token"] = response.json()['data']['refreshToken']
#     write_yaml({'headers':headers})
#     return headers
#
#
#
#
#
#
#
# @pytest.fixture(scope='session',autouse=True)
# def excute_dabates_sql():
#     clear_yaml()
#     clear_menzhen_yaml()
#     yield
#
#
#
