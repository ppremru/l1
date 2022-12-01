#!/bin/sh

# !!! ASSUMING python is python3 !!!!

# create a venv for build & packaging tools
python -m venv .env/build

# activate the venv
. .env/build/bin/activate

# install the setuptools build tool to the new environment
pip install build

# run build on the current directory
python -m build

# previous step will create a .tar.gaz & a .whl in ./dist
ls ./dist
