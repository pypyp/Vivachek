
import requests


class RequestMain:
    def __init__(self):
        """

        session管理器
        requests.session(): 维持会话,跨请求的时候保存参数
        """
        # 实例化session
        self.session = requests.session()

    def request_main(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        """

        :param method: 请求方式
        :param url: 请求地址
        :param params: 字典或bytes，作为参数增加到url中
        :param data: data类型传参，字典、字节序列或文件对象，作为Request的内容
        :param json: json传参，作为Request的内容
        :param headers: 请求头，字典
        :param kwargs: 若还有其他的参数，使用可变参数字典形式进行传递
        :return:
        """

        # 对异常进行捕获
        try:
            """

            封装request请求，将请求方法、请求地址，请求参数、请求头等信息入参。
            注 ：verify: True/False，默认为True，认证SSL证书开关；cert: 本地SSL证书。如果不需要ssl认证，可将这两个入参去掉
            """

            re_data = self.session.request(method, url, params=params, data=data, json=json, headers=headers,
                                           **kwargs).status_code
        # 异常处理 报错显示具体信息
        except Exception as e:
            # 打印异常
            print("请求失败：{0}".format(e))
        # 返回响应结果
        return re_data


headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Project": "vivachekcloud",
    "Platform": "3",
    "Version": "v1.7.0",
    "X-User-Agent": "ios/8.1",
    "Connection": "keep-alive",
    "Access-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI1NzgwMTc1Ny0xOTFiLTRmZjEtOGY4YS04ZWFkZDdjMzM2NjciLCJzdWIiOiJ2aXZhY2hlayIsImlzcyI6Imh0dHA6Ly9jbG91ZC52aXZhY2hlay5jb20uY24iLCJpYXQiOjE2NTQ1MDE1MTgsImV4cCI6MTY1NDUwODcxOH0.fTiRQMhdcuFhFqDsjBsKl1bIlHqB1BD2KAdidCdDP67ih3KgNrchOteubaV9jTLMW61PlV18G8CuHIo4HY5GCA"
}
if __name__ == '__main__':
    # 请求地址
    url = 'http://47.111.0.135:11157/vivachekcloud/api/paper/list'
    # 请求参数
    payload = {
        "pageNo": 1,
        "pageSize": 15,
        "depts": [
            "295946",
            "33"
        ]
    }
    # 请求头
    header = headers

    # 实例化 RequestMain()
    re = RequestMain()
    # 调用request_main，并将参数传过去
    request_data = re.request_main("post", url, json=payload, headers=header,timeout=2)
    # 打印响应结果
    print(request_data)
