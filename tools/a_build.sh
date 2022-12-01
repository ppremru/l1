#!/bin/sh


# create a venv for build & packaging tools
python3 -m venv .env/build

# activate the venv
. .env/build/bin/activate

# install the setuptools build tool to the new environment
pip3 install build

# run build on the current directory
python3 -m build

# previous step will create a .tar.gaz & a .whl in ./dist
ls ./dist
