from flask import render_template
from app import app


@app.route('/grid')
def hello_grid():
    return render_template("grid.html")