"""Utilities."""
from __future__ import absolute_import, division, print_function

import os

import pytoml

from .constants import CONF_FILE
from .errors import NotBumplusDir, VersionNotDefined


def bumplus_conf_file(dirname):
    """Return the path of Bumplus config file in DIRNAME."""
    return os.path.join(dirname, CONF_FILE)


def is_bumplus_dir(dirname):
    """Test whether Bumplus config file exist in DIRNAME."""
    return os.path.exists(bumplus_conf_file(dirname))


def check_bumplus_dir(dirname):
    """Raise an exception if DIRNAME does not have Bumplus config file."""
    if not is_bumplus_dir(dirname):
        raise NotBumplusDir()


def load_config(fname):
    """Return configuration from the file FNAME.

    If ``version`` is not defined, an exception will be raised.
    """
    with open(fname, encoding="utf-8") as f:
        config = pytoml.load(f)
    if "version" not in config:
        raise VersionNotDefined()
    return config


def dump_config(config, fname):
    """Write configuration into the file FNAME.

    If ``version`` is not defined, an exception will be raised.
    """
    if "version" not in config:
        raise VersionNotDefined()
    with open(fname, mode="w", encoding="utf-8") as f:
        return pytoml.dump(f, config)
