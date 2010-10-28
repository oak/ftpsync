from datetime import datetime

__author__ = 'adcarvalho'

class fileInfo(object):
    def __init__(self):
        self.baseDir = ''
        self.fileName = ''
        self.size = 0
        self.date = datetime.now()
