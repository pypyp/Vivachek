"""
  /**
     * 血糖详情数据格式校验模板
     */

"""
from compare.baseGlucose import BaseGlucose


class GluInfo(BaseGlucose):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "required": ["id", "timeType", "timeSlot", "unusual", "measureTime", "nurseId", "nurseName", "method",
                     "targetMaxValue", "targetMinValue"],
        "properties": {
            "userId": {
                "type": "string",
            },
            "comment": {
                "type": "string",
            },
            "targetMaxValue": {
                "type": "number",
            },
            "targetMinValue": {
                "type": "number",
            },
            "paperNum": {
                "type": "integer",
            },

        }
    }
    schema["properties"].update(BaseGlucose.BaseGlucose)
