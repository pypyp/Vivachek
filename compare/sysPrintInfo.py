"""
         /**
            * 打印模板接口数据格式校验
            */

    """


class SysPrintInfo(object):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "title": '配置',
        "description": '打印模板',
        "required": ["hosName", "codeBase", "qcCycle", "checkTaskt"],
        "properties": {
            "hosName": {"type": "string"},
            "codeBase": {"type": "integer"},
            "codePrefix": {"type": "string"},
            "codeSuffix": {"type": "string"},
            "qcCycle": {"type": "integer"},
            "qcTime": {"type": "string"},
            "checkTask": {"type": "integer"},
            "mzCodeBase": {"type": "integer"},
        }
    }
