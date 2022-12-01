#!/bin/sh

# !!! assuming python is python3 !!!!

# create a fresh clean venv 
python -m venv .env/deploy

# activate the venv
. .env/deploy/bin/activate

# install the wheel we built using pip
pip install dist/batman-0.0.1-py3-none-any.whl

# the CLI entrypoints listed in setup.cfg are now in .env the /bin dir
ls .env/deploy/bin/batman*

# 
echo "---- QUICK TEST ---- "
.env/deploy/bin/batman-usage
