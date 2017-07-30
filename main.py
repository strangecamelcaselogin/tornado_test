from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.web

import tornado.options
import tornado.autoreload

from handlers.all import HellowWorldHandler, FastHandler
from utils.loggers import app_log, gen_log, setup_loggers


def setup():
    setup_loggers()
    tornado.options.parse_command_line()
    # tornado.autoreload.start()  # Включение не дает запустить много процессов


def make_app():
    return tornado.web.Application([
        (r'/slow', HellowWorldHandler),
        (r'/fast', FastHandler)
    ])


if __name__ == '__main__':
    gen_log.info('prepare to start server...')
    setup()
    gen_log.info('setup ends...')

    app = make_app()

    try:
        server = HTTPServer(app)
        server.bind(8888)
        server.start(1)
        gen_log.info('start server...')

        IOLoop.current().start()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        pass  # todo log stacktrace

    finally:
        gen_log.info('stop server.')
        ioloop = IOLoop.instance()
        ioloop.add_callback(ioloop.stop)