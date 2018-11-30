from .db import *
from enum import Enum
from .coin import Coin


class User(Record):
    """
    用户信息
    """

    _table = 'user'
    _ddl = '''
    CREATE TABLE user(
        uid VARCHAR(20) PRIMARY KEY,
        real_name VARCHAR(20),
        nickname VARCHAR(20),
        password VARCHAR(20) NOT NULL,
        gender CHAR(1) CHECK (gender IN ('M', 'F') OR gender IS NULL),
        birth DATE,
        level INT DEFAULT 0,
        portrait VARCHAR(40),
        signature TEXT,
        address VARCHAR(20)
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

    def __str__(self):
        return str(self.to_tuple())

    def __repr__(self):
        return 'User' + repr(self.to_tuple())

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
    def register(cls, uid, real_name, nickname, password,gender):
        db = Database(cls._db)
        try:
            if cls.uid_exists(uid):
                return False
            temp = cls(uid=uid, real_name=real_name, nickname=nickname, password=password,gender=gender,
                       portrait="static/portrait/default.png")
            temp.insert(db)
            return True
        except Exception as e:
            print('last exec %s' % db.lastexec)
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
            """, uid) > 0

    @classmethod
    def get(cls, uid):
        db = cls.connect()
        users = db.query("""
            SELECT * FROM user
            WHERE uid = ?
            """, uid)
        if len(users) == 0:
            return None
        else:
            return cls.from_tuple(users[0])

    def recommend(self, count):
        """随机推荐用户"""

        db = self.connect()
        if self.gender == 'M':
            gender = 'F'
        else:
            gender = 'M'

        ans = db.query("""
            SELECT * FROM (
                SELECT * FROM user
                WHERE gender = ? AND uid NOT IN(
                    SELECT id2 FROM relation
                    WHERE id1 = ?
                )
            )
            ORDER BY RANDOM() LIMIT %d
        """ % count, (gender, self.uid))
        return User.translate(ans)

    def all_picked(self, uid):
        """返回pick的所有用户信息"""

        db = self.connect()

        ans = db.query("""
            SELECT * FROM user
            WHERE uid IN(
                SELECT id2 FROM relation
                WHERE id1 = ?
            )""", self.uid)

        return User.translate(ans)
    """
    计算等级
    """
    def calc_level(self):
        exp = Coin.get_exp(self.uid)
        """
        待改正
        """
        level_exp = [0, 100, 220, 364, 536, 742, 990, 1111111111]
        i = 0
        while exp > level_exp[i + 1]:
            i += 1
        level = i
        exp = exp - level_exp[i]
        self.level = level

    @classmethod
    def get_count(cls):
        db = cls.connect()
        return db.query("""
                        SELECT count(*) FROM user
                    """)[0][0]