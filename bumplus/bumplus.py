# -*- coding: utf-8 -*-

import os
import logging
import jinja2
from datetime import datetime

from .utils import bumplus_conf_file, check_bumplus_dir, load_config, dump_config
from .filters import filters
from .constants import CONF_FILE

logger = logging.getLogger(__package__)

class Bumplus(object):

    def __init__(self, path):
        check_bumplus_dir(path)
        self.path = path
        self.load_config()
        self.template_env = jinja2.Environment()
        self.template_env.filters.update(filters)

    def load_config(self):
        self.config = load_config(bumplus_conf_file(self.path))

    def replace_file(self, fname, file_config_list):
        path = os.path.join(self.path, fname)
        with open(path) as f:
            content_after = content_before = f.read()
        for file_config in file_config_list:
            search_tmpl = self.template_env.from_string(file_config['search'])
            search = search_tmpl.render(self.context)
            replace_tmpl = self.template_env.from_string(file_config['replace'])
            replace = replace_tmpl.render(self.context)
            content_after = content_after.replace(search, replace)
        if content_before != content_after:
            with open(path, 'w') as f:
                f.write(content_after)

    def bump_version(self, new_version):
        if self.config['version'] == new_version:
            return
        self.context = {
            'old_version': self.config['version'],
            'new_version': new_version,
            'now': datetime.now(),
            'utcnow': datetime.utcnow(),
        }
        for fname in self.config['files']:
            self.replace_file(fname, self.config['files'][fname])
        self.replace_file(CONF_FILE, [
            {
                'search': '{{old_version}}',
                'replace': '{{new_version}}',
            },
        ])
