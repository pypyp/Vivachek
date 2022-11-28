"""
         /**
            * 患者列表接口数据格式校验
            */

    """
from compare.page_respanse_list import PageRespanseList
from compare.patient_basic_info import PatientBasicInfo
from common.yaml_util import read_yaml


class Patinet(PageRespanseList, PatientBasicInfo):
    items = {
        "type": "object",
        "required": ["userId", "iptNum", "name", "gender", "iptTime", "deptId", "deptName"],
        "properties": {
            "value": {
                "type": "number",
                "maximum": 40,
                "minimun": 0.6
            },
            "measureTime": {
                "type": "string",
            },
            "timeType": {
                "type": "string",
            },
            "unusual": {
                "type": "integer",
            },
            "bedNum": {
                "type": "string",
            },
            "bedSort": {
                "type": "string",
            },
            "primayType": {"type": "integer",
                           },
        }

    }
    items['properties'].update(PatientBasicInfo.PatientBasicInfo)
    if read_yaml('headers')['Platform'] == 1:
        items["required"].append("primayType")

    @staticmethod
    def get():
        Patinet.schema["title"] = '住院患者'
        Patinet.schema["description"] = '住院患者'

        Patinet.schema['properties']['lists']['items'] = Patinet.items
        return Patinet.schema
