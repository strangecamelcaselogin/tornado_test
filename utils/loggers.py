from logging.handlers import RotatingFileHandler
import tornado.log
from tornado.log import LogFormatter


gen_log = tornado.log.gen_log
acc_log = tornado.log.access_log
app_log = tornado.log.app_log


def setup_loggers():
	rfh = RotatingFileHandler(r'logs/access.log')
	rfh.setFormatter(LogFormatter())
	acc_log.addHandler(rfh)
	acc_log.setLevel('WARN')

	rfh = RotatingFileHandler(r'logs/general.log')
	rfh.setFormatter(LogFormatter())
	gen_log.addHandler(rfh)
	gen_log.setLevel('INFO')

	rfh = RotatingFileHandler(r'logs/application.log')
	rfh.setFormatter(LogFormatter())
	app_log.addHandler(rfh)
	app_log.setLevel('INFO')
