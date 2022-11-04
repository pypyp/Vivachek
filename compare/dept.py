"""
  /**
     * 科室数据格式校验模板
     */

"""


class Dept(object):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '科室',
        "description": '科室列表',
        'data': {"type": "array",
                 "items": {
                     "type": "object",
                     "required": ["id", "name"],
                     "properties": {
                         "name": {"type": "string", },
                         "id": {
                             "type": "integer",
                         },

                     }
                 }
                 }
    }
