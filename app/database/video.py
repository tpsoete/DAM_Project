from .db import *


class Video(Record):
    """
    视频信息
    """

    _table = 'video'
    _ddl = '''
    CREATE TABLE video(
        uid VARCHAR(20),
        video TEXT PRIMARY KEY,
        level INT,
        FOREIGN KEY (uid) REFERENCES user (uid) ON DELETE CASCADE
    );
    '''

    def __init__(self, uid=None, video=None, level=None):
        Record.__init__(self)
        self.uid = uid
        self.video = video
        self.level = level

    @classmethod
    def from_tuple(cls, tpl):
        self = cls()
        self.uid, self.video, self.level = tpl
        return self

    def to_tuple(self):
        return self.uid, self.video, self.level

    @classmethod
    def get_video(cls, uid, level):
        '''获取符合权限的视频'''
        db = Database(cls._db)
        req = '''
        SELECT video
        FROM video
        WHERE uid='%s' AND
        level<=%s
        ''' % (uid, level)
        return db.query(req)
