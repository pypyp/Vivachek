"""
  /**
     * 血糖列表报告数据格式校验模板
     */

"""
from compare.baseGlucose import BaseGlucose



class Measure(BaseGlucose):
    """
      /**
         * APP血糖报告数据格式校验模板
         */

    """

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "required": ["userList", "gluList"],
        "userList": {"type": "array",
                     "items": {
                         "type": "object",
                         "required": ["userId", "name"],
                         "properties": {
                             "userId": {"type": "string", }, "name": {"type": "string", },

                         }
                     }},

        "gluList": {
            "required": ["pageNo", "pageSize", "count", "totalCount", 'totalPage'],
            "properties": {
                "pageNo": {"type": "integer"},
                "pageSize": {"type": "integer"},
                "count": {"type": "integer"},
                "totalCount": {"type": "integer"},
                "totalPage": {"type": "integer"},
                "int1": {"type": "integer"},
                "lists": {"type": "array", }

            }}}

    item = {
        "type": "object",
        "required": ["id", 'userId', "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName",
                     "deptId", "deptName", "name", "primayType", "valueUnit", "gender"],
        "properties": {
            "userId": {
                "type": "string",
            },
            "deptId": {
                "type": "string",
            },
            "name": {
                "type": "string",
            },
            "primayType": {
                "type": "string",
            },
            "gender": {
                "type": "string",
            }

        }}
    item["properties"].update(BaseGlucose.BaseGlucose)

    @staticmethod
    def get():
        Measure.schema["title"] = '血糖模块'
        Measure.schema["description"] = '当天血糖数据'

        Measure.schema['gluList']["properties"]['lists']['items'] = Measure.item
        return Measure.schema
