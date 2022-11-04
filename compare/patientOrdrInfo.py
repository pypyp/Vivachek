"""
         /**
            * 患者检测任务详情接口数据格式校验
            */

    """
from compare.orderBasicInfo import OrdertBasicInfo


class PatientOrderInfo(OrdertBasicInfo):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '住院模块',
        "description": '患者检测任务详情',
        "type": "object",
        "required": ["id", "userId", "iptNum", "name", "type", "timeType", "createTime",
                     "status", "startTime"],
        "properties":
            OrdertBasicInfo.OrderBasicInfo,


    }
