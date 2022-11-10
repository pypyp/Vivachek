import socket
from testCase.log import logger

"""
    检查服务后台服务是否启动
"""


def check_is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        logger.log_info.info('%d is open' % port)
        return True
    except Exception as e:
        logger.log_info.info('%d is down' % port)

        return False
