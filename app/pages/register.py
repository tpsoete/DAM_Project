from flask import render_template, request
from app import app
from app.database import *

import json
import time


@app.route('/register', methods=['POST', 'GET'])
def hello_register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        data = json.loads(request.get_data())
        print(data)
        username = data['id']
        realname = data['username']
        nickname = data['nikName']
        password = data['password']
        gender = data['gender']
        birth=data['birthday']
        timeStruct = time.strptime(birth, "%Y-%m-%d")
        timeStamp = int(time.mktime(timeStruct))
        if username is None or len(username) < 2:
            return "无效ID"
        result = User.register(uid=username, password=password, nickname=nickname, real_name=realname, gender=gender,
                               birth=timeStamp)
        print(result)
        if result:
            return "1"
        else:
            return "用户已存在"
