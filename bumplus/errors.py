"""Exception classes."""
from __future__ import absolute_import, division, print_function

from .constants import CONF_FILE


class BumplusError(Exception):
    """Base Bumplus exception."""


class NotBumplusDir(BumplusError):
    """Exception raised when Bumplus config file does not exist."""

    def __init__(self):
        """Initialize exception."""
        msg = f"Could not find {CONF_FILE}"
        super().__init__(msg)


class VersionNotDefined(BumplusError):
    """Exception raised when ``version`` is not defined in the config file."""

    def __init__(self):
        """Initialize exception."""
        msg = "Version not defined"
        super().__init__(msg)
