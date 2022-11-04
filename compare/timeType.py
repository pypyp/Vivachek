"""
         /**
            * 时段配置接口数据格式校验
            */

    """
class TimeType(object):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '时段',
        "description": '时段配置',
        'data': {"type": "array",
                 "items": {
                     "type": "object",
                     "required": ["id", "hosId", "name", "priority", "type", "inHos"],
                     "properties": {
                         "name": {"type": "string",
                                  },
                         "id": {
                             "type": "integer",
                         },
                         "hosId": {
                             "type": "string",
                         },
                         "priority": {
                             "type": "integer",
                         },
                         "inHos": {
                             "type": "integer",
                         },
                         "type": {
                             "type": "integer",
                         },
                         "analysisId": {
                             "type": "integer",
                         },

                     }
                 }
                 }
    }

    @staticmethod
    def webView():
        schema1 = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": '时段',
            "description": '时段配置',
            "type": "object",
            "properties": {
                "isInit": {"type": "integer"},

        }}

        schema1["properties"]["lists"]=TimeType.schema['data']
        return schema1


