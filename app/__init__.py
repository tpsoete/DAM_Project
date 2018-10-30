from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def create_app(debug=False):
    app.run(host="0.0.0.0", port=80, debug=debug)


if __name__ == '__main__':
    app.run(debug=True)