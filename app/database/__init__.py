from .user import *
from .album import *
from .video import *
from .relation import *
from .coin import *

__all__ = ['Database', 'Record',
           'User', 'Album', 'Video', 'Relation', 'Coin']


def reset_database():   # 初始化全部数据
    User.reset()
    Album.reset()
    Video.reset()
    Relation.reset()
    Coin.reset()


if __name__ == '__main__':
    reset_database()
