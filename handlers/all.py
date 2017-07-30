import ujson

import tornado.web

from utils.schema_validators import dvalidate
from voluptuous import Any, All, Required, PREVENT_EXTRA


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.args = {k: self.get_argument(k) for k in self.request.arguments}


class HellowWorldHandler(MainHandler):
    @dvalidate({Required('a'): str}, extra=PREVENT_EXTRA)
    def get(self):
        self.write('success: ' + str(self.args))


class FastHandler(MainHandler):
    def get(self):
        self.write('fast')
