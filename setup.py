from __future__ import absolute_import, division, print_function

import codecs
import glob
import itertools
import os
import re
import sys
from shutil import rmtree

from setuptools import Command, setup

__metaclass__ = type

__version__ = "0.7.0"


here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def status(s):
    print("\033[1m{0}\033[0m".format(s))


class CleanCommand(Command):
    description = "Clean caches"
    user_options = []  # type: list[tuple[str, str, str]]
    # Use builtin types
    #
    # https://stackoverflow.com/a/62033243
    # https://www.python.org/dev/peps/pep-0585/

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        status("Removing previous builds...")
        patterns = ("build", "dist", "*.egg", "*.egg-info")
        iglobs = (glob.iglob(pattern) for pattern in patterns)
        for d in itertools.chain.from_iterable(iglobs):
            try:
                rmtree(d)
            except Exception:
                if os.path.exists(d):
                    raise
        sys.exit()


description = "Bump the version in the project files."

with codecs.open("README.rst", encoding="utf-8") as readme_reader:
    long_description = re.sub(
        r"\`(.*)\<#.*\>\`\_", r"\1", readme_reader.read()
    )

setup(
    name="bumplus",
    version=__version__,
    url="https://github.com/dochang/bumplus",
    author="Wade Zhang",
    author_email="dochang@gmail.com",
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["bumplus"],
    entry_points={"console_scripts": ["bumplus = bumplus:main"]},
    install_requires=["pytoml", "Jinja2"],
    cmdclass={"clean": CleanCommand},
)
