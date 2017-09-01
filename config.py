from utils.cool_config import *


class Config(AbstractConfig):
    class server(Section):
        host = String
        port = Integer
        processes = Integer

    class loggers(Section):
        directory = String

        class app_log(Section):
            level = String
            file = String

        class gen_log(Section):
            level = String
            file = String

        class acc_log(Section):
            level = String
            file = String

config = Config()
