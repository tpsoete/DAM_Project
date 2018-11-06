from os.path import *


class Config:
    DEBUG = True

    APP_PATH = join(abspath(dirname(__file__)), 'app')
    STATIC_PATH = join(APP_PATH, 'static')
    PUBLIC_HOST = False

    CONFIG_TYPE = 'BASIC'


class DebugConfig(Config):

    CONFIG_TYPE = 'DEBUG'


class ReleaseConfig(Config):
    DEBUG = False

    PUBLIC_HOST = True

    CONFIG_TYPE = 'RELEASE'


class ActiveConfig(DebugConfig):
    """
    当前正在使用的配置
    """


config = ActiveConfig()
if __name__ == '__main__':
    print(config.APP_PATH)
    print(config.STATIC_PATH)
    print(type(config))
    print(config.__class__)
