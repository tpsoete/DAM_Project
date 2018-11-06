from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(type(config))
__import__('app.pages')


def create_app():
    debug = config.DEBUG
    if config.PUBLIC_HOST:
        app.run(host="0.0.0.0", port=80, debug=debug)
    else:
        app.run(debug=debug)

