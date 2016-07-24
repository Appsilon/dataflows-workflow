
# Dependencies

* python3.5
* python3.5-dev
* pip3.5

# Installation

* Install dependencies
  * For Ubuntu: `sudo ./install/install-ubuntu-dependencies.sh`
* Install Dataflows: `cd [dataflows-dir] && sudo ./install.sh` or `sudo ./install.sh [path-to-dataflows-dir]`

## Mac OS X

In case of problems with rpy2 library, please look at: https://gist.github.com/nickgravish/7ab136fc3bcbbac8316b

# Running

* Help: `dataflows -h`
* Show parsed dataflows.yml: `dataflows -c`
* Show version: `dataflows -v`
* Run workflow with default arguments: `dataflows` in the project dir (dataflows.yml must be present!)

Example:

`dataflows --model_parameters=1 --data=3 --sessionId=my_session`
