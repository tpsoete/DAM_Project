from flask import render_template
from app import app


@app.route('/register')
def hello_register():
    return render_template("register.html")
