from logging.handlers import RotatingFileHandler
from os.path import join as pjoin

import tornado.log
from tornado.log import LogFormatter

from config import config

gen_log = tornado.log.gen_log
acc_log = tornado.log.access_log
app_log = tornado.log.app_log


def setup_loggers():
	_loggers = config.loggers
	log_dir = _loggers.directory

	acc_log.setLevel(_loggers.acc_log.level)
	gen_log.setLevel(_loggers.gen_log.level)
	app_log.setLevel(_loggers.app_log.level)

	rfh = RotatingFileHandler(pjoin(log_dir, _loggers.acc_log.file))
	rfh.setFormatter(LogFormatter())
	acc_log.addHandler(rfh)

	rfh = RotatingFileHandler(pjoin(log_dir, _loggers.gen_log.file))
	rfh.setFormatter(LogFormatter())
	gen_log.addHandler(rfh)

	rfh = RotatingFileHandler(pjoin(log_dir, _loggers.app_log.file))
	rfh.setFormatter(LogFormatter())
	app_log.addHandler(rfh)
