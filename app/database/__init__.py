from app.database.user import *
from app.database.album import *
from app.database.video import *
from app.database.relation import *

__all__ = ['Database', 'Record',
           'User', 'Album', 'Video', 'Relation']


def reset_database():   # 初始化全部数据
    User.reset()
    Album.reset()
    Video.reset()
    Relation.reset()


if __name__ == '__main__':
    reset_database()
