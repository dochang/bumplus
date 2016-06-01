from .constants import CONF_FILE

class BumplusError(Exception):
    pass

class NotBumplusDir(BumplusError):
    def __init__(self):
        msg = 'Could not find {0}'.format(CONF_FILE)
        super(NotBumplusDir, self).__init__(msg)

class VersionNotDefined(BumplusError):
    def __init__(self):
        msg = 'Version not defined'
        super(VersionNotDefined, self).__init__(msg)
