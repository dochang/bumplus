from __future__ import absolute_import, division, print_function

import codecs
import os
import re

from setuptools import setup

__metaclass__ = type

__version__ = "0.7.0"


here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

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
)
