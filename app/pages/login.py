from flask import render_template, request, redirect
from app import app
from app.database import *


@app.route('/', methods=['GET', 'POST'])
def hello_masonry():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print("%s %s" % (username, password))
        result = User.login(username, password)
        if result == User.LoginStatus.SUCCESS:
            return "1"
        elif result == User.LoginStatus.NOT_EXIST:
            return "用户名不存在"
        else:
            return "密码错误"
