Bumplus
=======

Bumplus is a command line tool to bump your project version.

Prerequisites
-------------

Python 2.6, 2.7, 3.3, 3.4, 3.5

Usage
-----

Put a TOML_ file named :code:`.bumplus.toml` in the top-level directory of your project.  This file at least contains the following content:

.. code:: toml

  version = "<current_version>"

See Configuration_ for more config options.

.. _TOML: https://github.com/toml-lang/toml

Command line
~~~~~~~~~~~~

.. code:: shell

  cd <project root dir>
  bumplus <new_version>

Use :code:`bumplus --help` to display the help text.

Python
~~~~~~

.. code:: python

  import bumplus
  bp = bumplus.Bumplus('<project root dir>')
  bp.bump_version('<new_version>')

Example of :code:`.bumplus.toml`
--------------------------------

.. code:: toml

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

Every key is a relative path name.  The value of a key is an array of replacement config.  Every item of an array is an object which has two keys: :code:`search` and :code:`replace`.  The value of :code:`search` is the pattern to be replaced.  The value of :code:`replace` is the new text after replacing.

The contents of :code:`search` and :code:`replace` are Jinja2_ templates.  Several predefined variables can be used in the templates:

- :code:`old_version`
- :code:`new_version`
- :code:`now`
- :code:`utcnow`

:code:`now` and :code:`utcnow` are Python :code:`datetime` objects.

The Jinja2 templates also support a custom filter :code:`strftime`, which is used to format time such as :code:`now` and :code:`utcnow`.  The format string is the same as the parameter of :code:`strftime` method of Python :code:`datetime` object.

.. _Jinja2: http://jinja.pocoo.org/

.. attention:: Bumplus always replaces the current version in :code:`.bumplus.toml` after processing all files in the configuration.

License
-------

`MIT <https://dochang.mit-license.org/>`_
