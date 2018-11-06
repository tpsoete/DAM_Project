from flask import redirect
from app import app


@app.route('/about')
def hello_about():
    # TODO 关于我们
    return redirect('/')
