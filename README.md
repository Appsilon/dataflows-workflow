# Installation

## Mac OS X

In case of problems with rpy2 library, please look at: https://gist.github.com/nickgravish/7ab136fc3bcbbac8316b

* set environment variable `export DATAFLOWS_DIR=[absolute path to dataflows dir]`
* `./install.sh`

# Running

* Help: `dataflows -h`
* Show parsed dataflows.yml: `dataflows -c`
* Show version: `dataflows -v`
* Run workflow with default arguments: `dataflows` in the project dir (dataflows.yml must be present!)

Example:

`dataflows --model_parameters=1 --data=3 --sessionId=my_session`
