from flask import Flask
from config import *

app = Flask(__name__)


def create_app(argv):
    # 根据命令行参数选择配置
    global config
    if len(argv) >= 2 and argv[1] == '-r':
        config = ReleaseConfig()

    app.config.from_object(type(config))
    __import__('app.pages')

    debug = config.DEBUG
    if config.PUBLIC_HOST:
        app.run(host="0.0.0.0", port=config.PORT, debug=debug)
    else:
        app.run(debug=debug)

