"""Template filters."""
from __future__ import absolute_import, division, print_function


def strftime(value, format_spec="%x"):
    """Template filter to format data and time.

    :param value:
        A datatime object.
    :param format_spec:
        A format string which is the same as the parameter of ``strftime``
        method of Python ``datatime`` object.
    """
    return value.strftime(format_spec)


filters = {"strftime": strftime}
