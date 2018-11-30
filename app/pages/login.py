from flask import render_template, request
from app import app
from app.database import *

import json


@app.route('/')
def hello_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def check_pwd():
    data = json.loads(request.get_data())
    username = data['username']
    password = data['password']
    result = User.login(username, password)
    if result == User.LoginStatus.SUCCESS:
        return "1"
    elif result == User.LoginStatus.NOT_EXIST:
        return "用户名不存在"
    else:
        return "密码错误"
