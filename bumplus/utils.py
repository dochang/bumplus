from __future__ import absolute_import, division, print_function

import os

import pytoml

from .constants import CONF_FILE
from .errors import NotBumplusDir, VersionNotDefined

__metaclass__ = type


def bumplus_conf_file(path):
    return os.path.join(path, CONF_FILE)


def is_bumplus_dir(path):
    return os.path.exists(bumplus_conf_file(path))


def check_bumplus_dir(path):
    if not is_bumplus_dir(path):
        raise NotBumplusDir()


def load_config(path):
    with open(path) as f:
        config = pytoml.load(f)
    if "version" not in config:
        raise VersionNotDefined()
    return config


def dump_config(config, path):
    if "version" not in config:
        raise VersionNotDefined()
    with open(path, "w") as f:
        return pytoml.dump(f, config)
