from sqlite3 import *
from abc import abstractmethod
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
        """
        数据库查询，返回查询结果
        :param sql: SQL 查询语句
        :return: 查询结果（tuple 列表）
        """

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


class DBNull:
    """
    用于 INSERT 语句中将 Python 的 None 转化为 null 输出
    """
    def __init__(self):
        pass

    def __str__(self):
        return 'null'

    def __repr__(self):
        return 'null'

    @staticmethod
    def convert(tpl):
        """将 tuple 中的 None 替换为 null"""
        ret = []
        for item in tpl:
            if item is None:
                ret.append(DBNull())
            else:
                ret.append(item)
        return tuple(ret)


class Record:
    """
    数据库记录（抽象类）
    """

    _db = 'test.db'    # 数据库文件
    _table = None      # 表名
    _ddl = None        # 表定义（CREATE 语句）

    @classmethod
    def tablename(cls):
        """获得表名"""
        return cls._table

    @classmethod
    def reset(cls):
        """清除所有数据，重新建立表"""

        if cls._table is None or cls._ddl is None:
            print('表名或表定义为空')
            return

        db = Database(cls._db)
        db.modify("DROP TABLE IF EXISTS " + cls._table)
        db.modify(cls._ddl)

    def __init__(self, tpl):
        if type(tpl) != tuple:
            raise TypeError('Record 类型构造需要 tuple 类型')

    @abstractmethod
    def to_tuple(self):
        """转化为 tuple 用于 INSERT 语句"""
        pass

    def insert(self, database=None):
        """
        将数据插入到对应表中
        :param database: 指定数据库连接，不指定则新键
        """
        if database is not Database:
            database = Database(self._db)
        sql = "INSERT INTO %s VALUES %s" % (self._table, DBNull.convert(self.to_tuple()))
        database.modify(sql)
