from prepare import check_is_open, clear, get_user_info, get_patient, get_blood,get_temp_blood_info,get_order,get_paper_liquid_sn

from config.contast import Url, Header, Path, Client_Header, Config

from common.yaml_util import read_yaml

"获取当前登陆账号权限下的一些基础信息"


class BasicConfiguration(object):
    result = check_is_open.check_is_open(Config.IP, int(Config.PORT))
    if result is True:  # 判断后台服务是否正常
        clear.clear()  # 清空上次的测试数据
        get_user_info.get_user_info()  # 获取当前登陆账号的数据权限等
        if '10101' or '20101' in read_yaml('permissions'):
            user_id, ipt_time = get_patient.get_patient_info()  # 获取患者信息
            if user_id is not None:
                get_blood.get_blood_info(user_id,ipt_time)  # 获取患者的血糖信息
            # get_temp_blood_info.get_temp_blood_info()
            # get_order.get_order()




            if get_paper_liquid_sn.get_paper_liquid_sn() is True:
                pass #设备质控液试纸信息正确


        # elif '1010202' or '20104' in read_yaml('permissions'):
        #     pass
        #
        # if '105' or '205' in read_yaml('permissions'):
        #     pass


    else:
        print("请检查后台服务是否正常")
