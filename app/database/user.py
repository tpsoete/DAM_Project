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
        real_name VARCHAR(20),
        nickname VARCHAR(20),
        password VARCHAR(20) not null,
        gender CHAR(1),
        birth DATE,
        level int,
        portrait VARCHAR(40),
        signature VARCHAR(140),
        address VARCHAR(20),
        FOREIGN KEY (uid) REFERENCES album (uid),
        FOREIGN KEY (uid) REFERENCES video (uid),
        FOREIGN KEY (uid) REFERENCES relation (id1)
    );
    '''

    # def __init__(self, uid, nickname, password):
    #     self.uid = uid
    #     self.nickname = nickname
    #     self.password = password

    def __init__(self, tpl):
        Record.__init__()
        self.uid = tpl[0]
        self.nickname = tpl[1]
        self.password = tpl[2]
