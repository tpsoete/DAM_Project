from .db import *


class Relation(Record):
    """
    关系信息
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
        Record.__init__(self, tpl)
        self.id1, self.id2, self.level = tpl

    def to_tuple(self):
        return self.id1, self.id2, self.level
