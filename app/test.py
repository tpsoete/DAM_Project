from app.database import *
import app

import json


def getdata():
    User.reset()
    Relation.reset()

    User.register(uid='abc', real_name='xuboren', nickname='xxx', password='ppp')
    User.register(uid='abcde', real_name='xuboren3', nickname='xbr', password="'''")
    User.register(uid='aaa', real_name='名字', nickname='dao', password='123')

    db = User.connect()
    User(uid='123', real_name='名字', nickname='昵称', password='123', gender='M').insert(db)
    User(uid='456', real_name='撒士大夫十大', nickname='123456', password='456', gender='M').insert(db)
    User(uid='789', real_name='nae', nickname='!@#$%', password='789', gender='M').insert(db)
    User(uid='1234', real_name='名字', nickname='昵称', password='123', gender='F').insert(db)
    User(uid='1235', real_name='名字', nickname='昵称', password='123', gender='F').insert(db)
    User(uid='1236', real_name='名字', nickname='昵称', password='123', gender='F').insert(db)

    Relation(id1='123', id2='1234').insert(db)
    Relation(id1='123', id2='1235').insert(db)

    # for i in range(2000, 2100):
    #     if i % 2 == 0:
    #         g = 'M'
    #     else:
    #         g = 'F'
    #     User(uid=str(i), real_name=str(i), nickname=str(i+10000), password='123', gender=g).insert(db)

    User(uid='qwe', real_name='ewq', nickname='we', password='ewoiu', gender='F').insert(db)
    User(uid='rty', real_name='asd', nickname='agd', password='sdagkj', gender='F').insert(db)


if __name__ == '__main__':
    """网页测试"""
    # app.create_app()

    """数据库测试"""

    # getdata()

    db = Record.connect()

    print(Album.explore('1234'))

    # print(db.query('select * from user'))
    # print(db.query('select * from album'))
    # print(db.query('select * from relation'))



