from __future__ import absolute_import, division, print_function

__metaclass__ = type


def strftime(value, format="%x"):
    return value.strftime(format)


filters = {"strftime": strftime}
