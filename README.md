# Use PyPA build to create Python CLI application
To convert BAT csv file for Tackle.
bat-from-miro.csv --> bat-to-tackle.csv

## User Install 
```
# MVP - use env
python3 -m venv .env
. .env/bin/activate
pip install batman@git+http://github.com/ppremru/l1.git

# pip uninstall batman
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
