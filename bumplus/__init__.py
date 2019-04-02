from __future__ import absolute_import, division, print_function

from .bumplus import Bumplus
from .cli import main
from .errors import BumplusError, NotBumplusDir, VersionNotDefined
from .version import __version__

__metaclass__ = type


# Why do we export them again?  Because flake8 will report F401 if `__all__` is
# absent.  We have to declare `__all__` explicitly.  See [1] for details.
#
# [1]: https://bugs.launchpad.net/pyflakes/+bug/1178905/comments/4
__all__ = [
    "Bumplus",
    "BumplusError",
    "NotBumplusDir",
    "VersionNotDefined",
    "main",
    "__version__",
]
