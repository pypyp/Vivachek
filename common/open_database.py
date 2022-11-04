# coding=UTF-8
import os
import sys
import pymysql
from config.contast import Config
from testCase.log import logger
sys.path.append(r'' + os.path.abspath('../'))


class MysqlDb(object):

    def __init__(self):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(host=Config.database['MYSQL_HOST'], user=Config.database['MYSQL_USER'],
                                    password=Config.database['MYSQL_PASSWD'],
                                    charset='utf8', autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        print(self.conn)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        print(sql)
        logger.log_info.info('执行的sql%s', sql
                             )
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql

        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data
