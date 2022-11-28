"""
  /**
     * 控糖目标数据格式校验模板
     */

"""


class healthArchives(object):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '患者模块',
        "description": '控糖目标',
        'data': {"type": "array",
                 "items": {
                     "type": "object",
                     "required": ["timeName", "targetValueUp", "targetValueDown", "type"],
                     "properties": {
                         "timeName": {
                             "type": "string",
                         },
                         "targetValueUp": {
                             "type": "number",
                         },
                         "targetValueDown": {
                             "type": "number",

                         },
                         "type": {
                             "type": "integer",
                         },

                     }
                 }
                 }
    }
