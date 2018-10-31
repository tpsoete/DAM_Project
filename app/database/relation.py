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

    def __init__(self, id1=None, id2=None, level=None):
        Record.__init__(self)
        self.id1 = id1
        self.id2 = id2
        self.level = level

    @classmethod
    def from_tuple(cls, tpl):
        self = cls()
        self.id1, self.id2, self.level = tpl

    def to_tuple(self):
        return self.id1, self.id2, self.level
