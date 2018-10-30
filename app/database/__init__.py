from app.database.user import *
from app.database.album import *
from app.database.video import *

__all__ = ['User', 'Album', 'Video']


if __name__ == '__main__':
    db = Database('test.db')
    Video.reset()
    db.modify("insert into video values('11','/aaa','2')")
    print(db.query('select * from video'))
