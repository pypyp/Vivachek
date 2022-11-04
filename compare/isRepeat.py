"""
         /**
            * 校验数据方法
            */

    """
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError
from testCase.log import logger


class IsReapect(object):

    """
    校验数据是否重复
    """
    @staticmethod
    def dealList(data):
        Length = len(data)
        s = set()
        for i in data:
            i = str(i)
            s.add(i)
        if Length == len(s):
            return True
        else:
            return False

    """
        判断数据格式
    """
    @classmethod
    def isRepeat(cls, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    return IsReapect.dealList(value)
                # elif isinstance(value, dict):
                #     pass
                else:
                    return True
        elif isinstance(data, list):
            return IsReapect.dealList(data)

        else:
            print(data)

    """
        校验字段属性是否正确
    """
    @staticmethod
    def isValidate(data, cl):
        try:
            result = validate(instance=data, schema=cl, format_checker=draft7_format_checker)
            if result is None:
                return True
        except SchemaError as e:
            logger.log_info.error(
                "验证模式schema出错：\n出错位置：{}\n提⽰信息：{}".format(" --> ".join([i for i in e.path]), e.message))
        except ValidationError as e:
            logger.log_info.error(
                "json数据不符合schema规定：\n出错字段：{}\n提⽰信息：{}".format(" --> ".join([str(i) for i in e.path]), e.message))

    @staticmethod
    def multiPage(old_list, new_list):
        list1 = old_list + new_list
        list2 = list1
        return list2
