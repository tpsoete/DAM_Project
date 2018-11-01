from flask import render_template
from app import app


@app.route('/about')
def hello_about():
    return render_template("about.html")
