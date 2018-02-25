#!/bin/sh

set -e

pipenv run python setup.py sdist bdist_wheel
pipenv run twine upload dist/*
rm -rf build dist *.egg *.egg-info
