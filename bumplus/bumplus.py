# -*- coding: utf-8 -*-

"""Module of main class for Bumplus."""
from __future__ import absolute_import, division, print_function

import logging
import os
from datetime import datetime

import jinja2

from .constants import CONF_FILE
from .filters import filters
from .utils import bumplus_conf_file, check_bumplus_dir, load_config

logger = logging.getLogger(__package__)


class Bumplus:
    """Bumplus main class."""

    def __init__(self, path):
        """Initialize Bumplus.

        :param path:
            Top-level directory which contains Bumplus config file.
        """
        check_bumplus_dir(path)
        self.path = path
        self.load_config()
        self.template_env = jinja2.Environment(autoescape=True)
        self.template_env.filters.update(filters)

    def load_config(self):
        """Load config."""
        self.config = load_config(bumplus_conf_file(self.path))

    def replace_file(self, tmpl_vars, fname, file_config_list):
        """Replace patterns in the file.

        :param tmpl_vars:
            Template variables.
        :param fname:
            Name of the file.
        :param file_config_list:
            A list of patterns.
        """
        path = os.path.join(self.path, fname)
        with open(path, encoding="utf-8") as f:
            content_after = content_before = f.read()
        for file_config in file_config_list:
            tenv = self.template_env
            search_tmpl = tenv.from_string(file_config["search"])
            search = search_tmpl.render(tmpl_vars)
            replace_tmpl = tenv.from_string(file_config["replace"])
            replace = replace_tmpl.render(tmpl_vars)
            content_after = content_after.replace(search, replace)
        if content_before != content_after:
            with open(path, mode="w", encoding="utf-8") as f:
                f.write(content_after)

    def bump_version(self, new_version):
        """Bump current version to the new version."""
        if self.config["version"] == new_version:
            return
        tmpl_vars = {
            "old_version": self.config["version"],
            "new_version": new_version,
            "now": datetime.now(),
            "utcnow": datetime.utcnow(),
        }
        for fname in self.config["files"]:
            self.replace_file(tmpl_vars, fname, self.config["files"][fname])
        self.replace_file(
            tmpl_vars,
            CONF_FILE,
            [{"search": "{{old_version}}", "replace": "{{new_version}}"}],
        )
