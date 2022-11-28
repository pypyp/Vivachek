import requests

from common.yaml_util import read_yaml
from common.http_client import RequestMain

re = RequestMain()

a = {
    "pageNo": -1,
    "pageSize": 21,
    "deptId": "0003"
}

head = read_yaml('headers')
head["Access-Token"] = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIyMWZmOTNmZS0xN2M5LTQzNzAtOWUxNy0zNzQzYTJhYjVmOWMiLCJzdWIiOiIwMTEyODMiLCJpc3MiOiJodHRwOi8vY2xvdWQudml2YWNoZWsuY29tLmNuIiwiaWF0IjoxNjYwMDMzMjMzLCJleHAiOjE2NjAwNDA0MzN9.OY8Ccn05lMZY0dFs1AVXVbp1Unkb2SMke6ZM9bTmtU0nnQ6yzJyLCJYjvaeE9PBoKy4e7ea1TZvKfZ0Jvi7Y6g"
url = "http://47.111.0.135:11236/vivachekcloud/api/inhos/patient/list"
resoponse = re.request_main('post', url, headers=head,
                            json=a)

info={
  "timeType": "午餐后",
  "measureTime": "2022-08-09 16:02:04",
  "nurseId": "011283",
  "value": 9,
  "unusual": 1,
  "paperNum": 1,
  "valueUnit": 1,
  "method": 0
}

url1 = "http://47.111.0.135:11236/vivachekcloud/api/inhos/glu/add"
for i in resoponse['data']['lists']:
    info["userId"]= i['userId']
    resoponse = re.request_main('post', url1, headers=head,
                                json=info)
    print(resoponse)

