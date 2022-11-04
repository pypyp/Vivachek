"""
         /**
            * 质控统计接口数据格式校验
            */

    """
from compare.pageRespanseList import PageRespanseList
from compare.patientBasicInfo import PatientBasicInfo
from common.yaml_util import read_yaml


class QcStatistic(PageRespanseList):
    items = {
        "type": "object",
        "required": ["deptId", "deptName", "failCount", "lastOperationTime", "passRate", "totalCount"],
        "properties": {
            "deptId": {
                "type": "string",

            },
            "deptName": {
                "type": "string",
            },
            "failCount": {
                "type": "integer",
            },
            "lastOperationTime": {
                "type": "string",
            },
            "passRate": {
                "type": "integer",
            },
            "totalCount": {
                "type": "integer",

        },
        }
    }

    @staticmethod
    def get():
        QcStatistic.schema["title"] = '质控模块'
        QcStatistic.schema["description"] = '质控统计'

        QcStatistic.schema['properties']['lists']['items'] = QcStatistic.items
        return QcStatistic.schema
