from .db import *


class User(Record):
    """
    用户信息
    """

    # _db = 'data.db'
    _table = 'user'
    _ddl = '''
    CREATE TABLE user(
        uid VARCHAR(20) PRIMARY KEY,
        name VARCHAR(20)
    );
    '''

    def __init__(self, uid, name):
        Record.__init__()
        self.uid = uid
        self.name = name
