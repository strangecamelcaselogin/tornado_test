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


def make_app(rout_rules):
    return tornado.web.Application(rout_rules)


if __name__ == '__main__':
    port = 8888
    processes = 1
    routs = [(r'/slow', HellowWorldHandler),
             (r'/fast', FastHandler)]

    gen_log.info('prepare to start server...')
    setup()
    gen_log.info('setup ends...')

    app = make_app(routs)

    try:
        server = HTTPServer(app)
        server.bind(port)
        server.start(processes)
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