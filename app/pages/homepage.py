import json
import os

from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app.database import Relation, User, Album
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'bmp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/homepage', methods=['POST', 'GET'])  # 获取该用户所有已关注的用户信息
def picking():
    if request.method == 'GET':
        return render_template("homepage.html")

    else:
        data = json.loads(request.get_data())
        dtype = data['type']

        username = data['username']  # 输入

        if dtype == "picking":
            re = []
            picked_id = Relation.get_picked(username)
            for id_i in picked_id:
                picked_info = User.get(id_i[0])
                result = {
                    "portrait": picked_info.portrait,
                    "realname": picked_info.real_name,
                    "nickname": picked_info.nickname,
                    "follow": 1
                }
                result_json = json.dumps(result)
                re.append(result_json)
            return re

        elif dtype == "followers":
            re = []
            picked_id = Relation.get_follower(username)
            for id_i in picked_id:
                picked_info = User.get(id_i[0])
                relation = Relation.get_level(username, picked_info.uid)
                if relation != 0:
                    relation = 1
                result = {
                    "portrait": picked_info.portrait,
                    "realname": picked_info.real_name,
                    "nickname": picked_info.nickname,
                    "follow": relation
                }
                result_json = json.dumps(result)
                re.append(result_json)
            return re


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        print("1111")
        fileUpload = request.files['fileInput']
        # if not(fileUpload and allowed_file(fileUpload.filename)):
        #    return jsonify({"error": 1001, "msg": "type error"})
        print(request.values['type'])
        uploadPath = "app/static/upload/pic.png"
        fileUpload.save(uploadPath)



        # waterMark = './static/img/logo.png'
        # encode(uploadPath, waterMark, uploadPath)
        """写入数据库"""
        if request.values['type']=='file':
            """如果是图片"""
            dbPath=uploadPath[4:]
            Album('123', dbPath).insert()
        else:
            """如果是头像"""
            User.update('123','portrait',uploadPath)
        return jsonify({"code": 1111, "msg": "succeed!"})
