from flask import render_template, request
from app import app
from app.database import *

import json


@app.route('/', methods=['GET', 'POST'])
def hello_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = json.loads(request.get_data())
        print(data)
        username = data['username']
        password = data['password']
        print("%s %s" % (username, password))
        result = User.login(username, password)
        if result == User.LoginStatus.SUCCESS:
            return "1"
        elif result == User.LoginStatus.NOT_EXIST:
            return "用户名不存在"
        else:
            return "密码错误"
