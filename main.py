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
    host = 'localhost'
    port = 8888
    processes = 1
    routs = [(r'/slow', HellowWorldHandler),
             (r'/fast', FastHandler)]

    setup()
    gen_log.info('Setup ends.')

    gen_log.info('Prepare to start server at {}:{} in {} processes.'.format(host, port, processes))

    try:
        app = make_app(routs)
        server = HTTPServer(app)
        server.bind(port, address=host)
        server.start(processes)

        gen_log.info('Started.')
        IOLoop.current().start()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        pass  # todo log stacktrace

    finally:
        gen_log.info('Stop server.')
        ioloop = IOLoop.instance()
        ioloop.add_callback(ioloop.stop)
