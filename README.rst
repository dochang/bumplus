#########
 Bumplus
#########

.. image:: https://github.com/dochang/bumplus/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/dochang/bumplus/actions/workflows/ci.yml
   :alt: CI

.. image:: https://cloud.drone.io/api/badges/dochang/bumplus/status.svg
   :target: https://cloud.drone.io/dochang/bumplus
   :alt: Build Status

.. image:: https://codecov.io/gh/dochang/bumplus/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/dochang/bumplus
   :alt: Codecov

.. image:: https://img.shields.io/pypi/l/bumplus.svg
   :alt: PyPI - License
   :target: https://pypi.python.org/pypi/bumplus

.. image:: https://img.shields.io/pypi/wheel/bumplus.svg
   :alt: PyPI - Wheel
   :target: https://pypi.python.org/pypi/bumplus

.. image:: https://img.shields.io/pypi/format/bumplus.svg
   :alt: PyPI - Format
   :target: https://pypi.python.org/pypi/bumplus

.. image:: https://img.shields.io/pypi/pyversions/bumplus.svg
   :alt: PyPI - Python Version
   :target: https://pypi.python.org/pypi/bumplus

.. image:: https://badge.fury.io/py/bumplus.svg
   :target: https://badge.fury.io/py/bumplus

.. image:: https://requires.io/github/dochang/bumplus/requirements.svg?branch=master
   :target: https://requires.io/github/dochang/bumplus/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://pyup.io/repos/github/dochang/bumplus/shield.svg
   :target: https://pyup.io/repos/github/dochang/bumplus/
   :alt: Updates

.. image:: https://pyup.io/repos/github/dochang/bumplus/python-3-shield.svg
   :target: https://pyup.io/repos/github/dochang/bumplus/
   :alt: Python 3

.. image:: https://img.shields.io/badge/say-thanks-green.svg
   :target: https://saythanks.io/to/dochang
   :alt: Say Thanks!

Bumplus is a command line tool to bump your project version.

***************
 Prerequisites
***************

Python 3.6, 3.7, 3.8, 3.9

**************
 Installation
**************

.. code::

   pip install bumplus

*******
 Usage
*******

Put a TOML_ file named `.bumplus.toml` in the top-level directory of
your project. This file at least contains the following content:

.. code::

   version = "<current_version>"

See Configuration_ for more config options.

.. _toml: https://github.com/toml-lang/toml

Command line
============

.. code::

   cd <project root dir>
   bumplus <new_version>

Use `bumplus --help` to display the help text.

Python
======

.. code::

   import bumplus
   bp = bumplus.Bumplus('<project root dir>')
   bp.bump_version('<new_version>')

****************************
 Example of `.bumplus.toml`
****************************

.. code::

   version = '1.2.3'

   [[files."CHANGELOG.md"]]
   search = '''
   ## Unreleased
   '''
   replace = '''
   ## Unreleased

   ## {{new_version}} - {{utcnow | strftime("%Y-%m-%d")}}
   '''

   [[files."CHANGELOG.md"]]
   search = '''
   http://host/changelog/{{old_version}}.html
   '''
   search = '''
   http://host/changelog/{{new_version}}.html
   http://host/changelog/{{old_version}}.html
   '''

   [[files."LICENSE"]]
   search = '{{old_version}}'
   replace = '{{new_version}}'

   [[files."src/version.py"]]
   search = '{{old_version}}'
   replace = '{{new_version}}'

***************
 Configuration
***************

version
=======

A string that is the current version.

files
=====

A table which configures all files need to be modified.

Every key is a relative path name. The value of a key is an array of
replacement config. Every item of an array is an object which has two
keys: `search` and `replace`. The value of `search` is the pattern to be
replaced. The value of `replace` is the new text after replacing.

The contents of `search` and `replace` are Jinja2_ templates. Several
predefined variables can be used in the templates:

-  `old_version`
-  `new_version`
-  `now`
-  `utcnow`

`now` and `utcnow` are Python `datetime` objects.

The Jinja2 templates also support a custom filter `strftime`, which is
used to format time such as `now` and `utcnow`. The format string is the
same as the parameter of `strftime` method of Python `datetime` object.

.. _jinja2: http://jinja.pocoo.org/

.. attention::

   Bumplus always replaces the current version in `.bumplus.toml` after
   processing all files in the configuration.

*********
 License
*********

`MIT <https://dochang.mit-license.org/>`_
