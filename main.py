import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import options
from server import Application
from handlers import test_handlers
import logging

a = 1


def tick():
    global a
    print(a)
    a += 1


def main():
    http_server = tornado.httpserver.HTTPServer(Application)
    tornado.options.parse_command_line()
    http_server.listen(options.port, address='0.0.0.0')
    logging.info('%d 运行' % options.port)
    tornado.ioloop.PeriodicCallback(tick, 1000).start()
    tornado.ioloop.IOLoop.instance().start()

    # tornado.ioloop.IOLoop.instance()


if __name__ == '__main__':
    main()
