from ftp.client import Client
from ftp.listParser import parseDirAndFiles

__author__ = 'adcarvalho'

from config import settings, configFile

configFile.loadSettings()

ftpClient = Client(host=settings.host,
                   port=settings.port,
                   user=settings.user,
                   password=settings.password)

ftpClient.connect()

ftpDirs = []
ftpFiles = []

dirList = []

ftpClient.list(dirList)

parseDirAndFiles("/", dirList, ftpDirs, ftpFiles)

print "Dirs:"
for dirInfo in ftpDirs:
    print dirInfo.dirName, dirInfo.date

print "Files:"
for fileInfo in ftpFiles:
    print fileInfo.fileName, fileInfo.date

ftpClient.close()


