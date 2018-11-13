from app.database import *


def demo_data():
    User.reset()
    Relation.reset()
    Album.reset()
    db = User.connect()

    User(uid='123', real_name='名字', nickname='昵称', password='123', gender='M').insert(db)
    User(uid='1', real_name='名字', nickname='小蓉蓉', password='123', gender='F',
         portrait="static/img/1.png").insert(db)
    User(uid='2', real_name='名字', nickname='小琦琦', password='123', gender='F',
         portrait="static/img/2.jpg").insert(db)
    User(uid='3', real_name='名字', nickname='小远远', password='123', gender='F',
         portrait="static/img/3.png").insert(db)

    User(uid='4', real_name='名字', nickname='小萱萱', password='123', gender='F',
         portrait="static/img/big_portfolio_item_4.png").insert(db)

    Album(uid='1', photo="static/img/8.png").insert(db)
    Album(uid='2', photo="static/img/5.png").insert(db)
    Album(uid='4', photo="static/img/7.png").insert(db)
    Album(uid='3', photo="static/img/9.png").insert(db)
    Album(uid='2', photo="static/img/10.png").insert(db)
    Album(uid='3', photo="static/img/big_portfolio_item_6.png").insert(db)
    Album(uid='4', photo="static/img/big_portfolio_item_7.png").insert(db)
    Album(uid='4', photo="static/img/big_portfolio_item_8.png").insert(db)
    Album(uid='3', photo="static/img/big_portfolio_item_9.png").insert(db)


if __name__ == '__main__':
    demo_data()