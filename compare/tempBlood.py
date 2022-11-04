"""
         /**
            * 临时检测接口数据格式校验
            */

    """
from compare.pageRespanseList import PageRespanseList
from compare.baseGlucose import BaseGlucose


class TempBlood(PageRespanseList, BaseGlucose):
    items = {
        "type": "object",
        "required": ["id", "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName", "method"],
        "properties": {
            "comment": {
                "type": "string",
            },

        }}

    @staticmethod
    def get():
        TempBlood.schema["title"] = '血糖模块'
        TempBlood.schema["description"] = '临时检测列表'

        TempBlood.schema['properties']['lists']['items'] = TempBlood.items

        return TempBlood.schema
print(TempBlood.get())