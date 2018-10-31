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
        nickname VARCHAR(20),
        password VARCHAR(20) not null,
        real_name VARCHAR(20),
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
        Record.__init__(self, tpl)
        self.uid, self.nickname, self.password, self.real_name, self.gender, self.birth, self.level, \
            self.portrait, self.signature, self.address = tpl

    def to_tuple(self):
        return self.uid, self.nickname, self.password, self.real_name, self.gender, self.birth, self.level, \
               self.portrait, self.signature, self.address

    @classmethod
    def uid_exists(cls, uid_temp):  # 检测uid是否存在
        db = Database(cls._db)
        req = '''
        select uid from user
        where uid = 
        ''' + str(uid_temp)
        uid_sel = db.query(req)
        if len(uid_sel) == 0:
            return 0
        else:
            return 1

    @classmethod
    def login(cls, uid, password):  # 登陆，成功返回1，失败返回0
        db = Database(cls._db)
        req = '''
        select password from user
        where uid = 
        ''' + str(uid)
        password_sel = db.query(req)
        if len(password_sel) == 0:
            return 0
        if password_sel != password:
            return 0
        return 1

    @classmethod
    def register(cls, uid, password, nickname):
        db = Database(cls._db)
        if cls.uid_exists(uid) == 1:
            return 0
        temp = cls((uid, nickname, password,None,None,None,None,None,None,None))
        temp.insert(db)
        return 1
