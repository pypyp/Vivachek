"""
         /**
            * web单个患者检测任务接口数据格式校验
            */

    """
from compare.orderBasicInfo import OrdertBasicInfo


class PatientOrder(OrdertBasicInfo):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '住院模块',
        "description": '单个患者所有检测任务',
        "type": "object",
        "required": ["headInfo", "list"],

        "properties": {
            "headInfo":
                {"type": "object",
                 "required": ["num1", "num2", "num3", "num4"],
                 "properties": {
                     "num1": {
                         "type": "integer",
                     },
                     "num2": {
                         "type": "integer",
                     },
                     "num3": {
                         "type": "integer",
                     },
                     "num4": {
                         "type": "integer",
                     },
                 },

                 "lists": {"type": "array",
                           "items": {
                               "type": "object",
                               "required": ["id", "userId", "iptNum", "name", "type", "timeType", "createTime",
                                            "status",
                                            "startTime"],
                               "properties":
                                   OrdertBasicInfo.OrderBasicInfo,

                           }

                           }},

        }}
