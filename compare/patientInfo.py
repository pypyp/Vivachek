"""
         /**
            * 患者详情接口数据格式校验
            */

    """
from compare.patientBasicInfo import PatientBasicInfo
class PatientInfo(PatientBasicInfo):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '住院模块',
        "description": '患者信息',
        "type": "object",
        "required": ["userId", "iptNum", "name", "gender", "iptTime", "deptId", "deptName", "status", "patientId"],
        "properties": {
            # "userId": {
            #     "type": "string",
            # },
            # "patientId": {
            #     "type": "string",
            # },
            # "iptNum": {
            #     "type": "string",
            #
            # },
            # "name": {
            #     "type": "string",
            # },
            # "gender": {
            #     "type": "integer",
            # },
            #
            # "iptTime": {
            #     "type": "string",
            # },
            #
            # "deptId": {
            #     "type": "string",
            # },
            #
            # "deptName": {
            #     "type": "string",
            # },
            "phone": {
                "type": "string",
                "pattern": "^((13[0-9])|(14[579])|(15([0-3]|[5-9]))|(16[56])|(17[0-8])|(18[0-9])|(19[1589]))\\d{8}$"},
            "idCard": {
                "type": "string",
                "pattern": "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|"
            },
            # "birthday": {
            #     "type": "string",
            # },
            "bedNum": {
                "type": "string",
            },
            "bedSort": {
                "type": "string",
            },
            # "primayDocName": {
            #     "type": "string",
            # },
            # "primayDocId": {
            #     "type": "string",
            # },

            "primayNurseId": {
                "type": "string",
            },
            "primayNurseName": {
                "type": "string",
            },

            "status": {
                "type": "integer",
            },
            "hbalc": {
                "type": "number",
            },
            "diabetesType": {
                "type": "integer",
            },
            "nextUserId": {
                "type": "string",
            },
            "preUserId": {
                "type": "string",
            },

        }
    }
    schema['properties'].update(PatientBasicInfo.PatientBasicInfo)