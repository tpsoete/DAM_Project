from .db import *



class Coin(Record):
    """
    拥有硬币
    """

    _table = 'coin'
    _ddl = '''
    CREATE TABLE coin(
        uid VARCHAR(20) PRIMARY KEY,
        coin INT NOT NULL,
        exp INT NUT NULL,
        FOREIGN KEY (uid) REFERENCES user (uid) ON DELETE CASCADE
    );
    '''

    def __init__(self, uid=None, coin=0, exp=0):
        Record.__init__(self)
        self.uid = uid
        self.coin = coin
        self.exp = exp

    @classmethod
    def from_tuple(cls, tpl):
        self = cls()
        self.uid, self.coin, self.exp = tpl
        return self

    def to_tuple(self):
        return self.uid, self.coin, self.exp

    def __str__(self):
        return str(self.to_tuple())

    def __repr__(self):
        return 'User' + repr(self.to_tuple())

    @classmethod
    def get_coin(cls, uid):
        db = Database(cls._db)
        coin = db.query("""
                    SELECT coin FROM album
                    WHERE uid = ?
                """, uid)
        return coin[0][0]

    @classmethod
    def get_exp(cls, uid):
        db = Database(cls._db)
        exp = db.query("""
                    SELECT exp FROM album
                    WHERE uid = ?
                """, uid)
        return exp[0][0]

    """
    更改硬币数量（使用或获取）
    """
    @classmethod
    def change_coin(cls, uid, num):
        db = Database(cls._db)
        coin = Coin.get_coin(uid)
        coin += num
        if coin >= 0:
            db.query("""
                            UPDATE coin set ? FROM coin
                            WHERE uid=?
                        """, coin, uid)
            return True  # 硬币足够
        else:
            return False  # 硬币不足
