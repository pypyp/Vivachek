"""
         /**
            * 临时检测接口数据格式校验
            */

    """
from compare.page_respanse_list import PageRespanseList
from compare.base_glucose import BaseGlucose


class TempBlood(PageRespanseList, BaseGlucose):
    items = {
        "type": "object",
        "required": ["id", "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName", "method"],
        "properties": {


        }}

    @staticmethod
    def get():
        TempBlood.schema["title"] = '血糖模块'
        TempBlood.schema["description"] = '临时检测列表'

        TempBlood.schema['properties']['lists']['items'] = TempBlood.items

        return TempBlood.schema
