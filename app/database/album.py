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

    def __init__(self, tpl):
        Record.__init__(self, tpl)
        self.uid, self.photo, self.level = tpl

    def to_tuple(self):
        return self.uid, self.photo, self.level
