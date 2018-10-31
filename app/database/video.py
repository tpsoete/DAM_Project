from .db import *


class Video(Record):
    """
    视频信息
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
        Record.__init__(self, tpl)
        self.uid, self.video, self.level = tpl

    def to_tuple(self):
        return self.uid, self.video, self.level
