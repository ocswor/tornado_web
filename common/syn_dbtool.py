from collections import deque
import pymysql
import logging
from common import config


class DBPool(object):
    def __init__(self, host, port=3306, user='root', pwd=None, db_name='', maxconn=5, charset='utf8'):
        self.host, self.port, self.user, self.passwd, self.db, self.charset = host, port, user, pwd, db_name, charset
        self.maxconn = maxconn
        self.pool = deque(maxlen=maxconn)
        self.pool_dic = {}
        self.conn = None
        for i in range(maxconn):
            try:
                conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                       charset=self.charset)
                conn.autocommit(True)
                self.pool.append(conn)
            except Exception as e:
                raise IOError(e)

    def get_conn(self):
        if len(self.pool) != 0:
            conn = self.pool[0]
            conn.ping(reconnect=True)
            self.conn = conn
        else:
            logging.warning('连接池用完了')
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                   charset=self.charset)
            conn.autocommit(True)
        return conn

    def back_conn(self, conn):
        if len(self.pool) < 10:
            self.pool.append(conn)
        else:
            conn.close()
            conn = None


syn_dbtool = DBPool(host=config.DB_HOST, pwd=config.DB_PASS, db_name=config.DB_NAME, maxconn=10)
