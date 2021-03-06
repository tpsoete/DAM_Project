from sqlite3 import *
from abc import abstractmethod
import os
from datetime import datetime, date, time

from config import config


class Database:
    """
    SQLite 数据库访问接口
    """

    def __init__(self, filename, abspath=False):
        if abspath:
            self.filename = filename
        else:
            self.filename = os.path.join(config.STATIC_PATH, filename)
        self.conn = connect(self.filename)
        self.lastexec = "PRAGMA foreign_keys = ON"  # 开启外键约束
        self.conn.execute(self.lastexec)

    def __del__(self):
        self.conn.close()

    def query(self, sql, param=()):
        """
        数据库查询，返回查询结果
        :param sql: SQL 查询语句
        :param param: 需要插入的参数
        :return: 查询结果（tuple 列表）
        """

        if not isinstance(param, (tuple, list)):
            param = (param, )
        self.lastexec = sql, param
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, param)
        except Exception as e:
            print(e)
            raise
        ret = cursor.fetchall()
        cursor.close()
        return ret

    def modify(self, sql, param=()):
        """
        数据库修改，返回受影响的行数
        :param sql: SQL 修改语句
        :param param: 需要插入的参数
        :return: 受影响的行数，-1表示不是修改语句
        """

        if not isinstance(param, (tuple, list)):
            param = (param, )
        self.lastexec = sql, param
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, param)
        except Exception as e:
            print(e)
            self.conn.rollback()
            raise
        self.conn.commit()
        ret = cursor.rowcount
        cursor.close()
        return ret


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

    @classmethod
    def connect(cls):
        """连接对应的数据库"""

        return Database(cls._db)

    def __init__(self):
        pass

    # ---抽象数据处理---

    @classmethod
    @abstractmethod
    def from_tuple(cls, tpl):
        """从 tuple 构造"""
        pass

    @abstractmethod
    def to_tuple(self):
        """转化为 tuple 用于 INSERT 语句"""
        pass

    @staticmethod
    def sql_const(value):
        """
        将 Python 中的数据转化为 SQL 常量表示
        仅用于 insert_sql 和 insert 函数，其他情况建议使用 sqlite 自带转换
            None 替换为 null
            字符串转义（单引号）
            日期使用其字符串值
            其他：等于 repr(value) 的返回结果
        :param value: 要转化的值
        :return: 转化后的值
        """

        if value is None:
            return "NULL"

        elif isinstance(value, str):
            parts = value.split("'")
            ret = "'" + parts[0]
            for i in range(1, len(parts)):
                ret += "''" + parts[i]
            return ret + "'"

        elif isinstance(value, (date, time, datetime)):
            return "'%s'" % str(value)

        else:
            return repr(value)

    @staticmethod
    def convert(tpl):
        """
        将 to_tuple 的返回结果转化为 INSERT 语句需要的格式（字符串）
        """

        ret = '('
        first = True
        for item in tpl:
            if first:
                first = False
            else:
                ret += ', '
            ret += Record.sql_const(item)
        return ret + ')'

    def insert_sql(self):
        """插入该数据对应的 INSERT 语句"""
        return "INSERT INTO %s VALUES %s" % (self._table, Record.convert(self.to_tuple()))

    def insert(self, database=None):
        """
        将数据插入到对应表中
        :param database: 指定数据库连接，不指定则新建连接
        :return: 插入是否成功
        """

        if not isinstance(database, Database):
            database = Database(self._db)
        sql = self.insert_sql()
        return database.modify(sql) == 1

    @classmethod
    def translate(cls, result):
        """将 SELECT 语句返回的表转为对应类的 list"""

        if not isinstance(result, list):
            raise TypeError('需要list类型')

        ans = []
        for tpl in result:
            try:
                ans.append(cls.from_tuple(tpl))
            except ValueError:
                raise TypeError('接受类型 %s 与表数据 %s 不匹配' % (cls, tpl))

        return ans
