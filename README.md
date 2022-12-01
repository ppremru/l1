# Use PyPA build to create Python CLI applications
Deliberately simple example of how to create & package Python CLI
applications using the [PyPA setuptools build
tool](https://setuptools.readthedocs.io/).

## User Install 
```
pip install batman@git+http://github.com/ppremru/l1.git
```
## Developer Hints
### Build Step
```
tools/a_build.sh
```
### Deploy Steps
```
tools/b_deploy.sh
```
### Test Deploy Steps
```
tools/c_run.sh
```
### Run from command line
```
python -m batman --help
python -m batman --i data/hi --o data/bye
```
### Other stuff
```
# format code & pylint
pip install black
black 
pylint *.py
# tests are broken
# vscode is mean 
# force a clean build ... i know silly
rm -rf dist batman.egg-info/;tools/a_build.sh ;tools/b_deploy.sh ;tools/c_run.sh
```
