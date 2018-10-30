from .db import *


class Album(Record):
    """
    用户信息
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
        Record.__init__()
        self.uid = tpl[0]
        self.photo = tpl[1]
        self.level = tpl[2]
