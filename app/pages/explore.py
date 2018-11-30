from flask import render_template, request, redirect
from app import app
from app.database import *

import json


@app.route('/explore', methods=['GET', 'POST'])
def hello_explore():
    if request.method == 'GET':
        username = request.args.get('username')
        if username is None:
            # return redirect('/')
            pass
        return render_template("explore.html", username="123")
    else:
        data = json.loads(request.get_data())
        print(data)
        dtype = data['type']
        if dtype == "recommend":
            # 推荐用户
            uid = data['username']
            user = User.get(uid)
            ans = user.recommend(3)
            result = []
            for rec in ans:
                assert isinstance(rec, User)
                result.append({
                    "username": rec.uid,
                    "nickname": rec.nickname,
                    "portrait": rec.portrait
                })
            # print(result)
            return json.dumps(result)

        elif dtype == "explore":
            uid = data['username']
            ans = Album.explore(uid, 9)

            result = []
            for al in ans:
                assert isinstance(al, Album)
                result.append({
                    "nickname": User.get(al.uid).nickname,
                    "img": al.photo
                })
            # print(result)
            return json.dumps(result)

        elif dtype == "view":
            un = data['username']
            print(un)
            return "123"

        else:
            return None




