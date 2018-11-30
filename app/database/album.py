from .db import *
from .user import User


class Album(Record):
    """
    相册信息
    """

    _table = 'album'
    _ddl = '''
    CREATE TABLE album(
        uid VARCHAR(20) NOT NULL,
        photo TEXT PRIMARY KEY,
        level INT DEFAULT 0,
        FOREIGN KEY (uid) REFERENCES user (uid) ON DELETE CASCADE
    );
    '''

    def __init__(self, uid=None, photo=None, level=0):
        Record.__init__(self)
        self.uid = uid
        self.photo = photo
        self.level = level

    @classmethod
    def from_tuple(cls, tpl):
        self = cls()
        self.uid, self.photo, self.level = tpl
        return self

    def to_tuple(self):
        return self.uid, self.photo, self.level

    def __str__(self):
        return str(self.to_tuple())

    def __repr__(self):
        return 'User' + repr(self.to_tuple())

    @classmethod
    def get_all(cls, uid, level=255, count=9):
        """获取符合权限的相片"""

        db = Database(cls._db)
        ans = db.query("""
            SELECT * FROM album
            WHERE uid = ? AND level <= ?
            ORDER BY RANDOM() LIMIT %d
        """ % count, (uid, level))
        return Album.translate(ans)

    @classmethod
    def explore(cls, uid, count=9):
        """随机选取，不能取到自己的"""

        db = cls.connect()
        ans = db.query("""
            SELECT * FROM album
            WHERE uid != ? AND level = 0
            ORDER BY RANDOM() LIMIT %d
        """ % count, uid)
        return Album.translate(ans)

    @classmethod
    def get_count(cls):
        db = cls.connect()
        return db.query("""
                    SELECT count(*) FROM album
                """)[0][0]
