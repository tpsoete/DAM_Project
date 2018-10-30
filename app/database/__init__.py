from app.database.user import *
from app.database.album import *

__all__ = ['User', 'Album']


if __name__ == '__main__':
    db = Database('test.db')
    Album.reset()
    db.modify("insert into album values('11','/aaa','2')")
    print(db.query('select * from album'))
