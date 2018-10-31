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

    def __init__(self, uid=None, real_name=None, nickname=None, password=None, gender=None,
                 birth=None, level=None, portrait=None, signature=None, address=None):
        Record.__init__(self)
        self.uid = uid
        self.real_name = real_name
        self.nickname = nickname
        self.password = password
        self.gender = gender
        self.birth = birth
        self.level = level
        self.portrait = portrait
        self.signature = signature
        self.address = address

    @classmethod
    def from_tuple(cls, tpl):
        self = cls()
        self.uid, self.real_name, self.nickname, self.password, self.gender, self.birth, self.level,\
            self.portrait, self.signature, self.address = tpl

    def to_tuple(self):
        return self.uid, self.real_name, self.nickname, self.password, self.gender, self.birth, self.level,\
               self.portrait, self.signature, self.address
