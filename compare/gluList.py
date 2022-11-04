"""
  /**
     * 血糖列表报告数据格式校验模板
     */

"""
from compare.baseGlucose import BaseGlucose
from compare.pageRespanseList import PageRespanseList


class GluList(BaseGlucose, PageRespanseList):
    items = {
        "type": "object",
        "required": ["id", "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName", "userId"],
        "properties": {
            "comment": {
                "type": "string", },
            "userId": {
                "type": "string",
            }

        }}
    items['properties'].update(BaseGlucose.BaseGlucose)
    @staticmethod
    def get():
        GluList.schema["title"] = '血糖模块'
        GluList.schema["description"] = '患者血糖列表'

        GluList.schema['properties']['lists']['items'] = GluList.items
        return GluList.schema


