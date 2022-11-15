from testCase.log import logger
from compare.isRepeat import IsReapect


class Encapsulation(object):
    """
      /**
         * 查询接口校验数据 只有一页
         */

    """

    @staticmethod
    def repeatOne(url, info, response, cl):
        if info['parame'] is None:
            info['parame'] = "不传参数"

        """
              /**
                 * 用于判断接口无数据，参数错误的情况
                 */

            """
        if 'data' not in response.keys():
            try:
                logger.log_info.info('---->接口:%s开始校验:校验返回状态码,返回参数类型必须返回的参数，返回的参数是否重复', url)
                assert response['msg'] == info['result']['msg']
                assert response['code'] == info['result']['code']
                logger.log_info.info('---->接口:%s校验通过', url)
            except AssertionError as e:
                logger.log_info.error("接口:{0},校验失败：{1}".format(url, e), exc_info=1)
                raise
            logger.log_info.info('---->接口%s结束一次用例测试' % url)

        else:
            data = response['data']
            result = IsReapect.isValidate(data, cl)
            result1 = IsReapect.isRepeat(data)
            # print(result1)
            try:
                logger.log_info.info('---->接口:%s开始校验:校验返回状态码,返回参数类型必须返回的参数，返回的参数是否重复', url)
                assert response['msg'] == info['result']['msg']
                assert response['code'] == info['result']['code']
                assert result is True
                assert result1 is True
                logger.log_info.info('---->接口:%s校验通过', url)

            except AssertionError as e:
                logger.log_info.error("接口:{0},校验失败：{1}".format(url, e), exc_info=1)
                raise
            logger.log_info.info('---->接口%s结束一次用例测试' % url)

    """
         /**
            * 查询接口校验数据 有多页
            */

    """

    @staticmethod
    def repeatTwo(url, info, response, old_list, cl):
        data = response['data']
        new_list = data['lists']
        result = IsReapect.isValidate(data, cl)
        list2 = IsReapect.multiPage(old_list, new_list)
        list3 = list2
        result1 = IsReapect.isRepeat(list3)
        assert result1 is True
        try:
            logger.log_info.info('---->接口:%s开始校验:校验返回状态码,返回参数类型必须返回的参数，返回的参数是否重复', url)
            assert response['code'] == info['result']['code']
            assert response['msg'] == info['result']['msg']
            assert result is True
            assert result1 is True
            logger.log_info.info('---->接口:%s校验通过', url)
        except AssertionError as e:
            logger.log_info.error("接口:{0},校验失败：{1}".format(url, e), exc_info=1)
            raise
        logger.log_info.info('---->接口%s结束一次用例测试' % url)
        return list3

    """
             /**
                * 增删改接口校验数据 
                */

        """

    @staticmethod
    def repeatThree(url, info, response):
        if "parame" not in info.keys():
            info['parame'] = {}

        try:
            logger.log_info.info('---->接口:%s开始校验:校验返回状态码，以及数据库校验', url)
            print(response)
            assert response['code'] == info['result']['code']
            assert response['msg'] == info['result']['msg']

        except AssertionError as e:
            logger.log_info.error("接口:{0},校验失败：{1}".format(url, e), exc_info=1)
            raise
