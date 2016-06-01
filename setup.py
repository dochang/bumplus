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

long_description = re.sub(
  "\`(.*)\<#.*\>\`\_",
  r"\1",
  open('README.rst').read()
)

setup(
    name='bumplus',
    version='0.0.2',
    author='Desmond O. Chang',
    author_email='dochang@gmail.com',
    license='MIT',
    description=description,
    long_description=long_description,
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
