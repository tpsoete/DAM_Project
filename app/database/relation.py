from .db import *


class Relation(Record):
    """
    关系信息
    """

    # _db = 'data.db'
    _table = 'relation'
    _ddl = '''
    CREATE TABLE relation(
        id1 VARCHAR(20) NOT NULL,
        id2 VARCHAR(20) NOT NULL,
        level int,
        PRIMARY KEY(id1,id2)
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
        return self

    def to_tuple(self):
        return self.id1, self.id2, self.level

    @classmethod
    def get_level(cls, uid1, uid2):
        db = cls.connect()
        req = '''
        SELECT level
        FROM relation
        WHERE id1=%s AND
        id2=%s
        ''' % (uid1, uid2)
        level = db.query(req)
        if len(level) == 0:
            return None
        return level[0][0]
