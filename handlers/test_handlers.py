# encoding: utf-8
__author__ = 'Eric'
__date__ = '2017/12/16 上午10:24'

import logging
from datetime import datetime

import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler

from common.base import BaseJsonRequestHandler
from common.db import db_pool
from common.syn_dbtool import syn_dbtool
from common.utils import request_wrap


class TestHandler(RequestHandler):

    def get(self):
        print(datetime.now())
        # time.sleep(1)
        # start = datetime.now()
        n = 0
        # for i in range(10000000):
        #     n = n+ 1
        # end = datetime.now()
        # print end - start
        # time.sleep(1)
        for i in range(5000):
            n = n + 1

        client = AsyncHTTPClient()
        client.fetch('http://127.0.0.1:6005/', callback=self.on_response)
        # client.fetch('http://baidu.com', callback=self.on_response)
        # time.sleep(2)

    def on_response(self, response):
        print(response.code)
        self.write('ok')
        self.finish()


@request_wrap(r"/api/test/")
class Test2Handler(BaseJsonRequestHandler):
    async def get(self, *args, **kwargs):
        # cursor = await db_pool.execute("SELECT owner_pid FROM app_club WHERE cid=%s AND state=1", (20895,))
        # club = cursor.fetchone()
        # logging.info(club)

        #

        connection = syn_dbtool.get_conn()
        with connection.cursor() as cursor:
            # 读取单个记录
            sql = 'SELECT owner_pid FROM app_club WHERE cid=%s AND state=1' % (20895,)
            cursor.execute(sql)
            result = cursor.fetchone()
            logging.info(result)

        self.json_response(data_dict={'status': 1})
