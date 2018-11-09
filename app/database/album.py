from .db import *


class Album(Record):
    """
    相册信息
    """

    _table = 'album'
    _ddl = '''
    CREATE TABLE album(
        uid VARCHAR(20) NOT NULL,
        photo TEXT PRIMARY KEY,
        level INT,
        FOREIGN KEY (uid) REFERENCES user (uid) ON DELETE CASCADE
    );
    '''

    def __init__(self, uid=None, photo=None, level=None):
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

    @classmethod
    def get_album(cls, uid, level):
        """获取符合权限的相片"""
        db = Database(cls._db)
        req = '''
            SELECT photo
            FROM album
            WHERE uid=%s AND
            level<=%s
            ''' % (uid, level)
        return db.query(req)
