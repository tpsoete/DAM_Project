from app.database import *

if __name__ == '__main__':
    db = Database('test.db')
    Relation.reset()
    Relation('11','12',3).insert(db)
    print(Relation.get_level('11','12'))
