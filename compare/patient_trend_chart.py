"""
         /**
            * 血糖统计图接口数据格式校验
            */

    """
from compare.base_glucose import BaseGlucose


class PatientTrendChart(BaseGlucose):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '血糖模块',
        "description": '趋势图',
        "type": "object",
        "required": ["tableInfo"],
        "tableInfo": {
            "type": "object",
            "required": ["averageValue", "highCount", "lowCount", "maxValue", "minValue", "normalCount",
                         "targetMaxValue", "targetMinValue", "totalCount"],
            "averageValue": {"type": "number", },
            "highCount": {"type": "integer", },
            "lowCount": {"type": "number", },
            "maxValue": {"type": "integer", },
            "minValue": {"type": "number", },
            "normalCount": {"type": "integer", },
            "targetMaxValue": {"type": "number", },
            "targetMinValue": {"type": "number", },
            "totalCount": {"type": "integer", },

        },
        "list": {"type": "array",
                 "items": {
                     "type": "object",
                     "required": ["id", "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName",
                                  "userId"],
                     "properties": {
                         "userId": {"type": "string", },

                     }
                 }}}

    schema['list']["items"]["properties"].update(BaseGlucose.BaseGlucose)
