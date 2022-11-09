"""Template filters."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


def strftime(value, format="%x"):
    """Template filter to format data and time.

    :param value:
        A datatime object.
    :param format:
        A format string which is the same as the parameter of ``strftime``
        method of Python ``datatime`` object.
    """
    return value.strftime(format)


filters = {"strftime": strftime}
