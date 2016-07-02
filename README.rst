Bumplus
=======

.. image:: https://travis-ci.org/dochang/bumplus.svg?branch=master
    :target: https://travis-ci.org/dochang/bumplus

.. image:: https://codecov.io/gh/dochang/bumplus/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dochang/bumplus
    :alt: Codecov

.. image:: https://badge.fury.io/py/bumplus.svg
    :target: https://badge.fury.io/py/bumplus

.. image:: https://requires.io/github/dochang/bumplus/requirements.svg?branch=master
    :target: https://requires.io/github/dochang/bumplus/requirements/?branch=master
    :alt: Requirements Status

Bumplus is a command line tool to bump your project version.

Prerequisites
-------------

Python 2.6, 2.7, 3.3, 3.4, 3.5

Usage
-----

Put a TOML_ file named `.bumplus.toml` in the top-level directory of your project.  This file at least contains the following content:

::

  version = "<current_version>"

See Configuration_ for more config options.

.. _TOML: https://github.com/toml-lang/toml

Command line
~~~~~~~~~~~~

::

  cd <project root dir>
  bumplus <new_version>

Use `bumplus --help` to display the help text.

Python
~~~~~~

::

  import bumplus
  bp = bumplus.Bumplus('<project root dir>')
  bp.bump_version('<new_version>')

Example of `.bumplus.toml`
--------------------------------

::

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

Configuration
-------------

version
~~~~~~~

A string that is the current version.

files
~~~~~

A table which configures all files need to be modified.

Every key is a relative path name.  The value of a key is an array of replacement config.  Every item of an array is an object which has two keys: `search` and `replace`.  The value of `search` is the pattern to be replaced.  The value of `replace` is the new text after replacing.

The contents of `search` and `replace` are Jinja2_ templates.  Several predefined variables can be used in the templates:

- `old_version`
- `new_version`
- `now`
- `utcnow`

`now` and `utcnow` are Python `datetime` objects.

The Jinja2 templates also support a custom filter `strftime`, which is used to format time such as `now` and `utcnow`.  The format string is the same as the parameter of `strftime` method of Python `datetime` object.

.. _Jinja2: http://jinja.pocoo.org/

.. attention:: Bumplus always replaces the current version in `.bumplus.toml` after processing all files in the configuration.

License
-------

`MIT <https://dochang.mit-license.org/>`_
