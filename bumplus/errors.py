"""Exception classes."""
from __future__ import absolute_import, division, print_function

from .constants import CONF_FILE

__metaclass__ = type


class BumplusError(Exception):
    """Base Bumplus exception."""

    pass


class NotBumplusDir(BumplusError):
    """Exception raised when Bumplus config file does not exist."""

    def __init__(self):
        """Initialize exception."""
        msg = "Could not find {0}".format(CONF_FILE)
        super(NotBumplusDir, self).__init__(msg)


class VersionNotDefined(BumplusError):
    """Exception raised when ``version`` is not defined in the config file."""

    def __init__(self):
        """Initialize exception."""
        msg = "Version not defined"
        super(VersionNotDefined, self).__init__(msg)
