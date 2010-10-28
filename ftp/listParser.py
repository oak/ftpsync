from ftp.dirInfo import dirInfo
from ftp.fileInfo import fileInfo
from datetime import datetime

__author__ = 'adcarvalho'


def parseDirAndFiles(baseDir, sourceList, targetDirList, targetFileList):
    for line in sourceList:
        if ("<DIR>" in line):
            targetDirList.append(parseDir(line))
        else:
            targetFileList.append(parseFile(line))

def parseDir(dirLine):
    dir = dirInfo()

    dir.date = getDate(dirLine)
    dir.dirName = getName(dirLine)

    return dir

def parseFile(fileLine):
    file = fileInfo()

    file.date = getDate(fileLine)
    file.size = getFileSize(fileLine)
    file.fileName = getName(fileLine)

    return file

def getDate(line):
    return datetime.strptime(line[0:17], "%m-%d-%y  %I:%M%p")

def getFileSize(line):
    return int(line[18:38].strip())

def getName(line):
    return line[39:]

