from sqlite3 import *
import os

from config import config


class Database:
    """
    SQLite 数据库访问接口
    """

    def __init__(self, filename, abspath=False):
        if abspath:
            self.filename = filename
        else:
            self.filename = os.path.join(config.static_path, filename)
        self.conn = connect(self.filename)

    def __del__(self):
        self.conn.close()

    def query(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            raise
        ret = cursor.fetchall()
        cursor.close()
        return ret

    def modify(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
            raise
        self.conn.commit()
        ret = cursor.rowcount
        cursor.close()
        return cursor.rowcount


class Record:
    """
    数据库记录（抽象类）
    """

    _db = 'test.db'    # 数据库文件
    _table = None      # 表名
    _ddl = None        # 表定义（CREATE语句）

    @classmethod
    def tablename(cls):
        return cls._table

    @classmethod
    def reset(cls):
        """清除所有数据，重新建立表"""

        if cls._table is None or cls._ddl is None:
            print('表名或表定义为空')
            return

        db = Database(cls._db)
        db.modify('DROP TABLE IF EXISTS ' + cls._table)
        db.modify(cls._ddl)

    def __init__(self):
        pass

