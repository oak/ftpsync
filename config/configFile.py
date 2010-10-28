__author__ = 'developer'

import ConfigParser, settings

config = ConfigParser.RawConfigParser()

def saveSettings():
    if (not config.has_section("Config")):
        config.add_section('Config')

    config.set('Config', 'host', settings.host)
    config.set('Config', 'port', settings.port)
    config.set('Config', 'user', settings.user)
    config.set('Config', 'password', settings.password)

    with open('settings.cfg', 'wb') as configFile:
        config.write(configFile)

def loadSettings():
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')

    if (config.has_section("Config")):
        settings.host = config.get('Config', 'host')
        settings.port = config.getint('Config', 'port')
        settings.user = config.get('Config', 'user')
        settings.password = config.get('Config', 'password')