from tornado.options import define
import os
import tornado.web

define('port', default=8001, type=int)
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'static_url_prefix': '/static/',
}

Application = tornado.web.Application(**settings)
