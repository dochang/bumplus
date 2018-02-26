from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import codecs
import re
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

description = 'Bump the version in the project files.'

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = re.sub(
        "\`(.*)\<#.*\>\`\_",
        r"\1",
        f.read()
    )

about = {}
with open(os.path.join(here, 'bumplus', 'version.py')) as f:
    exec(f.read(), about)

setup(
    name='bumplus',
    version=about['__version__'],
    url='https://github.com/dochang/bumplus',
    author='Desmond O. Chang',
    author_email='dochang@gmail.com',
    license='MIT',
    description=description,
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['bumplus'],
    entry_points={
        'console_scripts': [
            'bumplus = bumplus:main',
        ],
    },
    install_requires=[
        'pytoml',
        'Jinja2',
    ],
    tests_require=['tox'],
    cmdclass={
        'test': Tox,
    },
)
