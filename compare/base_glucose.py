"""
  /**
     * 血糖数据通用字段
     */

"""


class BaseGlucose(object):
    BaseGlucose = {
        "id": {
            "type": "integer",
        },
        "timeType": {
            "type": "string",

        },
        "timeSlot": {
            "type": "string",
        },
        "unusual": {
            "type": "integer",
        },
        "measureTime": {
            "type": "string",
        },
        "nurseId": {
            "type": "string",
        },
        "nurseName": {
            "type": "string",
        },
        "method": {
            "type": "integer",
        },
        "deviceNo": {
            "type": "string",
        },

        "value": {
            "type": "number",
        },
        "valueUnit": {
            "type": "integer",
        },

        "comment": {
            "type": "string",
        }
    }
