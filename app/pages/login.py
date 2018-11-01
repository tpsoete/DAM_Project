from flask import render_template, request, redirect
from app import app
from app.database import *


@app.route('/', methods=['GET', 'POST'])
def hello_masonry():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get("password")
        if User.login(username, password) == User.LoginStatus.SUCCESS:
            return redirect('/main')
        else:
            return render_template('login.html')