from __future__ import absolute_import, division, print_function

import codecs
import glob
import itertools
import os
import re
import sys
from shutil import rmtree
from subprocess import call

from setuptools import Command, setup

__metaclass__ = type


here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def status(s):
    print("\033[1m{0}\033[0m".format(s))


class CleanCommand(Command):
    description = "Clean caches"
    user_options = []

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


class UploadCommand(Command):
    description = "Publish the package"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        status("Uploading the package to PyPI via twine...")
        cmd = ["twine", "upload"]
        pkgs = glob.glob("dist/*")
        cmd.extend(pkgs)
        sys.exit(call(cmd))


description = "Bump the version in the project files."

with codecs.open("README.rst", encoding="utf-8") as f:
    long_description = re.sub(r"\`(.*)\<#.*\>\`\_", r"\1", f.read())

about = {}
with open(os.path.join("bumplus", "version.py")) as f:
    exec(f.read(), about)

setup(
    name="bumplus",
    version=about["__version__"],
    url="https://github.com/dochang/bumplus",
    author="Wade Zhang",
    author_email="dochang@gmail.com",
    license="MIT",
    description=description,
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bumplus"],
    entry_points={"console_scripts": ["bumplus = bumplus:main"]},
    install_requires=["pytoml", "Jinja2"],
    cmdclass={"clean": CleanCommand, "upload": UploadCommand},
)
