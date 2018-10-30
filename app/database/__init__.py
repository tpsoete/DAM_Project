from app.database.user import *

__all__ = ['User']


if __name__ == '__main__':
    db = Database('test.db')
    # User.reset()
    # db.modify("insert into user values('0','aaa','123456')")
    # db.modify("insert into user values('1','bbb','654321')")
    print(db.query('select * from user'))
