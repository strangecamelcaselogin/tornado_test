import yaml


class BasicConfig:
    _default_path = r''

    @property
    def default_path(self):
        return self._default_path

    @default_path.setter
    def default_path(self, value):
        raise AttributeError('Can not set default path in runtime.')

    def __init__(self, *args, **kwargs):
        raise NotImplementedError


class AppConfig(BasicConfig):
    _default_path = r'configs/app.yml'
    host = ''
    port = 0
    debug = False
    processes = 0


class LoggersConfig(BasicConfig):
    _default_path = r'configs/loggers.yml'
    pass
