# ml-cli
Creating a simple Machine Learning command line interface that will provide output.

## Examples of auto-generated reports from the ml-cli can be found here:
https://jameshtwose.github.io/ml-cli/

## To run the CLI (without a python install):
- download the latest .dmg file from the releases (https://github.com/jameshtwose/ml-cli/releases)
- to install click and drag the .dmg to your Applications
- because the mlcli App is not available in the App store, you will get a "this app is not trusted" error when trying to open it
- to overcome this go to "Privacy & Security" in your settings and allow the app
- go back to your Applications in finder, right-click on the app and select "New Terminal at Folder"
- this will open the terminal at the root of the app
- run the help command from this folder using:
  - `./Contents/MacOS/mlcli --help` or 
  - `./Contents/MacOS/mlcli descriptives --help`
  - `./Contents/MacOS/mlcli make-report --help`


## To run the CLI from python do the following:
- clone the repo:
  - `git clone git@github.com:jameshtwose/ml-cli.git`
- install the python requirements (consider using an env)
  - `pip install -r requirements.txt`
- to run the descriptives:
  - `python mlcli.py descriptives data/penguins.csv`
- to create a machine learning classification report:
  - `python mlcli.py make-report data/penguins.csv --outcome=species` or
  - `python mlcli.py make-report data/penguins.csv --outcome=sex --export-name=docs/penguins_classification_report.html`
- for help on the `CLI` run:
  - `python mlcli.py --help`
