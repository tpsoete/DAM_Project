from .db import *


class Video(Record):
    """
    用户信息
    """

    # _db = 'data.db'
    _table = 'video'
    _ddl = '''
    CREATE TABLE video(
        uid VARCHAR(20) PRIMARY KEY,
        video VARCHAR(40),
        level int
    );
    '''

    def __init__(self, tpl):
        Record.__init__()
        self.uid = tpl[0]
        self.video = tpl[1]
        self.level = tpl[2]
