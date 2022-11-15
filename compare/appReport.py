"""
  /**
     * APP血糖报告数据格式校验模板
     */

"""
from compare.baseGlucose import BaseGlucose



class AppGluReport(BaseGlucose):
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "data": {"type": "array",
                 "items": {
                     "type": "object",
                     "required": ["date"],
                     "properties": {
                         "date": {"type": "string", },

                     }
                 }}}

    item = {
        "type": "object",
        "required": ["id", 'userId', "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName",
                     "deviceNo", "valueUnit", "comment"],
        "properties": {
            "userId": {
                "type": "string",
            }

        }}
    item["properties"].update(BaseGlucose.BaseGlucose)

    @staticmethod
    def get():
        AppGluReport.schema["title"] = '血糖模块'
        AppGluReport.schema["description"] = '患者血糖报告'


        return AppGluReport.schema
