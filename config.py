from os.path import *


class Config:

    app_path = join(abspath(dirname(__file__)), 'app')
    static_path = join(app_path, 'static')

    def __init__(self):
        pass


config = Config()
if __name__ == '__main__':
    print(config.app_path)
    print(config.static_path)
