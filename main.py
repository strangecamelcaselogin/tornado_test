import tornado.autoreload
import tornado.log
import tornado.options
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from config import config

from handlers.all import HellowWorldHandler, FastHandler
from loggers import gen_log, setup_loggers


def setup():
    setup_loggers()
    tornado.log.enable_pretty_logging()
    # tornado.options.parse_command_line()
    # tornado.autoreload.start()  # Включение не дает запустить много процессов


def make_app(rout_rules):
    return tornado.web.Application(rout_rules)


if __name__ == '__main__':
    config.load('configs/config.yml')

    host = config.server.host
    port = config.server.port
    processes = config.server.processes

    routs = [(r'/slow', HellowWorldHandler),
             (r'/fast', FastHandler)]

    setup()
    gen_log.info('Setup ends.')

    try:
        gen_log.info('Prepare to start server at {}:{} in {} processes.'.format(host, port, processes))
        app = make_app(routs)
        server = HTTPServer(app)
        server.bind(port, address=host)
        server.start(processes)

        gen_log.info('Started.')
        IOLoop.current().start()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        gen_log.error(e)

    finally:
        gen_log.info('Stop server.')
        ioloop = IOLoop.instance()
        ioloop.add_callback(ioloop.stop)
