import tornado.web
from voluptuous import Required, PREVENT_EXTRA

from loggers import app_log
from utils.schema_validators import dvalidate


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.args = {k: self.get_argument(k) for k in self.request.arguments}


class HellowWorldHandler(MainHandler):
    @dvalidate({Required('a'): str}, extra=PREVENT_EXTRA)
    def get(self):
        self.write('success: ' + str(self.args))


class FastHandler(MainHandler):
    def get(self):
        app_log.info('fast handler')
        self.write('fast')
        app_log.info('fast handler end.')
