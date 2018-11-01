from .db import *
from enum import Enum


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
        uid_sel = db.query("""
            select uid from user
            where uid = ?
            """, uid_temp)
        if len(uid_sel) == 0:
            return False
        else:
            return True

    class LoginStatus(Enum):
        SUCCESS = 0
        NOT_EXIST = 1
        WRONG = 2

    @classmethod
    def login(cls, uid, password):
        """登陆，返回登录状态"""
        db = Database(cls._db)
        password_sel = db.query("""
            SELECT password FROM user
            WHERE uid = ?
            """, uid)
        if len(password_sel) == 0:
            return cls.LoginStatus.NOT_EXIST
        if password_sel[0][0] != password:
            return cls.LoginStatus.WRONG
        return cls.LoginStatus.SUCCESS

    @classmethod
    def register(cls, uid, real_name, nickname, password):
        db = Database(cls._db)
        try:
            if cls.uid_exists(uid):
                return False
            temp = cls(uid=uid, real_name=real_name, nickname=nickname, password=password)
            temp.insert(db)
            return True
        except Exception as e:
            print('last exec %s ' % db.lastexec)
            raise

    @classmethod
    def update(cls, uid, part, value):
        """更新数据"""
        db = Database(cls._db)
        if not cls.uid_exists(uid):
            return False
        db.modify("""
            UPDATE user 
            SET %s = ?
            WHERE uid = ?
            """ % part, (value, uid))
        return True

    @classmethod
    def delete(cls, uid):
        """注销账户"""
        db = Database(cls._db)
        return db.modify("""
            DELETE FROM user
            WHERE uid = ?
            """, uid) == 1
