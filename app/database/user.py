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
        self.uid, self.real_name, self.nickname, self.password, self.gender, self.birth, self.level, \
        self.portrait, self.signature, self.address = tpl
        return self

    def to_tuple(self):
        return self.uid, self.real_name, self.nickname, self.password, self.gender, self.birth, self.level, \
               self.portrait, self.signature, self.address

    @classmethod
    def uid_exists(cls, uid_temp):
        """检测uid是否存在"""
        db = Database(cls._db)
        req = '''
        select uid from user
        where uid = 
        ''' + str(uid_temp)
        uid_sel = db.query(req)
        if len(uid_sel) == 0:
            return False
        else:
            return True

    @classmethod
    def login(cls, uid, password):
        """登陆，成功返回1，失败返回0"""
        db = Database(cls._db)
        req = '''
        select password from user
        where uid = 
        ''' + str(uid)
        password_sel = db.query(req)
        if len(password_sel) == 0:
            return False
        if password_sel[0][0] != password:
            return False
        return True

    @classmethod
    def register(cls, uid, password, nickname):
        db = Database(cls._db)
        if cls.uid_exists(uid):
            return False
        temp = cls((uid, nickname, password, None, None, None, None, None, None, None))
        temp.insert(db)
        return True

    @classmethod
    def update(cls, uid, part, value):
        """更新数据"""
        db = Database(cls._db)
        if not cls.uid_exists(uid):
            return False
        req = '''
        UPDATE user 
        SET %s = %s
        WHERE uid = %s
        ''' % (part, value, uid)
        print(req)
        db.modify(req)
        return True

    @classmethod
    def delete(cls, uid):
        """注销账户"""
        db = Database(cls._db)
        if not cls.uid_exists(uid):
            return False
        req = '''
                DELETE FROM user
                WHERE uid = %s
                ''' % uid
        print(req)
        db.modify(req)
        return True
