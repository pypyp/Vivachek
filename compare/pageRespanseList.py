"""
  /**
     * lists数据通用模板
     */

"""


class PageRespanseList(object):
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["pageNo", "pageSize", "count", "totalCount", 'totalPage'],
        "properties": {
            "pageNo": {"type": "integer"},
            "pageSize": {"type": "integer"},
            "count": {"type": "integer"},
            "totalCount": {"type": "integer"},
            "totalPage": {"type": "integer"},
            "int1": {"type": "integer"},
            "lists": {"type": "array"
                      },

        }
    }
