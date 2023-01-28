# ml-cli
Creating a simple Machine Learning command line interface that will provide output.

## Examples of auto-generated reports from the ml-cli can be found here:
https://jameshtwose.github.io/ml-cli/

## To run the CLI do the following:
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
