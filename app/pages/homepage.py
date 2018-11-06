from flask import render_template
from app import app


@app.route('/homepage')
def hello_home():
    return render_template("homepage.html")
