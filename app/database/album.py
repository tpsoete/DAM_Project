from .db import *


class Album(Record):
    """
    相册信息
    """

    # _db = 'data.db'
    _table = 'album'
    _ddl = '''
    CREATE TABLE album(
        uid VARCHAR(20) PRIMARY KEY,
        photo VARCHAR(40),
        level int
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

    def to_tuple(self):
        return self.uid, self.photo, self.level
