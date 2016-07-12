#!/bin/sh

set -e

cd $(dirname $0)

venv_dir=venv/release
dist_dir=dist

rm -rf $dist_dir $venv_dir

virtualenv $venv_dir
. $venv_dir/bin/activate
pip install -U twine

python setup.py sdist
twine upload $dist_dir/*
