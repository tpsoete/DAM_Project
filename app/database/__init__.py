from app.database.user import *
from app.database.album import *
from app.database.video import *
from app.database.relation import *

__all__ = ['User', 'Album', 'Video', 'Relation']


if __name__ == '__main__':
    db = Database('test.db')
    Relation.reset()
    db.modify("insert into relation values('11','12','2')")
    print(db.query('select * from relation'))
