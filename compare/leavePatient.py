"""
         /**
            * 出院接口数据格式校验
            */

    """
from compare.pageRespanseList import PageRespanseList
from compare.patientBasicInfo import PatientBasicInfo


class leavePatinet(PageRespanseList, PatientBasicInfo):
    items = {
        "type": "object",
        "required": ["userId", "iptNum", "name", "gender", "iptTime", "deptId", "leaveTime"],
        "properties": {
            "phone": {
                "type": "string",
                "pattern": "^((13[0-9])|(14[579])|(15([0-3]|[5-9]))|(16[56])|(17[0-8])|(18[0-9])|(19[1589]))\\d{8}$"
            },
            "iptGluValue": {
                "type": "number",
                "maximum": 40,
                "minimun": 0.6
            },
            " leaveGluValue": {
                "type": "number",
                "maximum": 40,
                "minimun": 0.6

            },
            "operator": {
                "type": "string",
            },
            "leaveTime": {
                "type": "string",
            },
        }}
    items['properties'].update(PatientBasicInfo.PatientBasicInfo)

    @staticmethod
    def get():
        leavePatinet.schema["title"] = '住院患者'
        leavePatinet.schema["description"] = '出院患者列表'

        leavePatinet.schema['properties']['lists']['items'] = leavePatinet.items

        return leavePatinet.schema
