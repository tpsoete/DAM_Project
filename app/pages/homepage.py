from flask import render_template
from app import app


@app.route('/homepage', methods=['GET', 'POST'])
def hello_homepage():
    return render_template("homepage.html")
