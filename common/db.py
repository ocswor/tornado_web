#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import tormysql
from tornado import gen
from common import config

db_pool = tormysql.helpers.ConnectionPool(
    max_connections=20,  # max open connections
    idle_seconds=7200,  # conntion idle timeout time, 0 is not timeout
    wait_connection_timeout=3,  # wait connection timeout
    host=config.DB_HOST,
    user=config.DB_USER,
    passwd=config.DB_PASS,
    db=config.DB_NAME,
    charset="utf8"
)


@gen.coroutine
def execute_update(sql, value, callback):
    tx = yield db_pool.begin()
    try:
        yield db_pool.execute(sql, value)
        yield tx.commit()
        if callback:
            callback(None)
    except Exception as e:
        logging.exception("Exception type: %s" % type(e).__name__)
        yield tx.rollback()
        if callback:
            callback(e)
