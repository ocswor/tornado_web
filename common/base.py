from tornado.web import RequestHandler
import json


class BaseJsonRequestHandler(RequestHandler):

    def json_response(self, data_dict):
        self.add_header("Content-Type", "application/json;charset=utf-8")
        self.write(json.dumps(data_dict, ensure_ascii=False))
