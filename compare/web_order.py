"""
         /**
            * web检测任务接口数据格式校验
            */

    """
from compare.page_respanse_list import PageRespanseList
from compare.order_basic_info import OrdertBasicInfo


class WebOrder(PageRespanseList, OrdertBasicInfo):
    items = {
        "type": "object",
        "required": ["id", "userId", "iptNum", "name", "type", "timeType",
                     "status",
                     "startTime", "deptId", "deptName","testNum","execNum"],
        "properties":{
                "bedNum": {
                    "type": "string",
                },
                "deptId": {
                    "type": "string",
                },
                "deptName": {
                    "type": "string",
                },
                "execNum": {
                    "type": "integer",
                },
                "gender": {
                    "type": "integer",
                },

                "showType": {
                    "type": "integer",
                },

                "testNum": {
                    "type": "integer",
                },

                "timeSlot": {
                    "type": "string",
                },

            }

    }
    items["properties"].update(OrdertBasicInfo.OrderBasicInfo)
    @staticmethod
    def get():
        WebOrder.schema["title"] = '检测任务'
        WebOrder.schema["description"] = 'web检测任务列表'

        WebOrder.schema['properties']['lists']['items'] = WebOrder.items

        return WebOrder.schema