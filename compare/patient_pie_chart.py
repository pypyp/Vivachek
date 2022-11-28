"""
         /**
            * 血糖趋势图数据格式校验
            */

    """
class PatientPieChart(object):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '血糖模块',
        "description": '统计图',
        "type": "object",
        "required": ["highCount", "lowCount", "normalCount", "totalCount"],
        "properties": {
            "highCount": {
                "type": "integer",
            },
            "lowCount": {
                "type": "integer",
            },
            "normalCount": {
                "type": "integer",
            },
            "totalCount": {
                "type": "integer",
            },
        }
    }