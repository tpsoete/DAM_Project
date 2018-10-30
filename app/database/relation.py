from .db import *


class Relation(Record):
    """
    用户信息
    """

    # _db = 'data.db'
    _table = 'relation'
    _ddl = '''
    CREATE TABLE relation(
        id1 VARCHAR(20) PRIMARY KEY,
        id2 VARCHAR(20) NOT NULL,
        level int
    );
    '''

    def __init__(self, tpl):
        Record.__init__()
        self.id1 = tpl[0]
        self.id2 = tpl[1]
        self.level = tpl[2]
