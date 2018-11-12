from flask import render_template, request
from app import app
from app.database import *

import json


@app.route('/register', methods=['GET', 'POST'])
def hello_register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        data = json.loads(request.get_data())
        username = data['username']
        realname = data['realname']
        nickname = data['nickname']
        password = data['password']
        user = User(uid=username, password=password, nickname=nickname, real_name=realname)
        if User.uid_exists(username):
            return "用户已存在"
        else:
            user.insert()
            return "创建成功"

