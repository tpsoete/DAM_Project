from flask import Flask

app = Flask(__name__)
__import__('app.pages')


def create_app(debug=False):
    app.run(host="0.0.0.0", port=80, debug=debug)


def debug_app():
    app.run(debug=True)

