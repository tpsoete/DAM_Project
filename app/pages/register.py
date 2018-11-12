from flask import render_template, request
from app import app
from app.database import *

import json


@app.route('/register', methods=['POST', 'GET'])
def hello_register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        data = json.loads(request.get_data())
        username = data['username']
        realname = data['realname']
        nickname = data['nickname']
        password = data['password']
        result = User.register(uid=username, password=password, nickname=nickname, real_name=realname)
        if result:
            return "1"
        else:
            return "用户已存在"
