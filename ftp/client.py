__author__ = 'adcarvalho'

from ftplib import FTP

class Client(object):

    def __init__(self, host='', port=22, user='', password=''):
        self.client = FTP(host=host)
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        self.client.login(user=self.user, passwd=self.password)
        self.client.set_pasv(False)

    def list(self, dirList):
        self.client.dir(dirList.append)

    def close(self):
        self.client.quit()