from os.path import *


class Config:
    DEBUG = True    # 是否开启调试模式

    APP_PATH = join(abspath(dirname(__file__)), 'app')  # app模块路径
    STATIC_PATH = join(APP_PATH, 'static')  # static 路径
    PUBLIC_HOST = False     # 是否监听所有IP（公网访问）
    PORT = 5000     # 服务器部署的端口


class DebugConfig(Config):
    pass


class ReleaseConfig(Config):
    DEBUG = False

    PUBLIC_HOST = True
    PORT = 80


config = DebugConfig()
