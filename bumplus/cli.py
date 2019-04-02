from __future__ import absolute_import, division, print_function

import argparse
import logging
import os

from .bumplus import Bumplus
from .errors import NotBumplusDir
from .utils import is_bumplus_dir
from .version import __version__

__metaclass__ = type


logger = logging.getLogger(__package__)


def is_fs_root(path):
    return path == "/"


def find_bumplus_topdir(path):
    found = is_bumplus_dir(path)
    while not found and not is_fs_root(path):
        path = os.path.normpath(os.path.join(path, ".."))
        found = is_bumplus_dir(path)
    if found:
        return path
    raise NotBumplusDir()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Bump version.")
    parser.add_argument("new_version", help="New version")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {0}".format(__version__),
        help="Display bumplus version",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Display more information",
    )
    args = parser.parse_args(argv)

    log_levels = (logging.WARNING, logging.INFO, logging.DEBUG)
    log_level_idx = min(args.verbose, len(log_levels) - 1)
    log_level = log_levels[log_level_idx]
    logger.setLevel(log_level)
    if len(logger.handlers) == 0:
        log_handler = logging.StreamHandler()
        logger.addHandler(log_handler)

    path = find_bumplus_topdir(os.getcwd())
    bp = Bumplus(path)
    bp.bump_version(args.new_version)
