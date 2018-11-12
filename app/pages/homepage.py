from flask import render_template, request
from app import app


@app.route('/homepage', methods=['GET', 'POST'])
def hello_home():
    if request.method == 'GET':
        return render_template("homepage.html")
    else:
        return "None"

