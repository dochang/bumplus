"""Helper scripts."""

import sys
from pathlib import Path
from shutil import rmtree

from invoke import task

import bumplus


@task
def start(c):
    """Run bumplus without installing it."""
    # pylint: disable=unused-argument
    argv_index = sys.argv.index("--") + 1
    argv = sys.argv[argv_index:] if "--" in sys.argv else []
    bumplus.main(argv)


@task
def clean(c):
    """Clean packaging generated files."""
    # pylint: disable=unused-argument
    patterns = ("build", "dist", "*.egg", "*.egg-info")
    globs = [Path(".").glob(p) for p in patterns]
    flatten = [p for glob in globs for p in glob]
    for p in flatten:
        if p.is_dir():
            rmtree(p)
        else:
            p.unlink()
