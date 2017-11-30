
# Dependencies

* python3.5
* python3.5-dev
* pip3.5

```
sudo apt-get install python3.5 python3.5-dev python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip3.5
```

# Installation

* Install dependencies
  * For Ubuntu: `sudo ./install/install-ubuntu-dependencies.sh`
* Install Dataflows:
  * `cd [dataflows-dir] && sudo ./install.sh`
  * or `sudo ./install.sh [path-to-dataflows-dir]`

## Mac OS X

In case of problems with rpy2 library, please look at: https://gist.github.com/nickgravish/7ab136fc3bcbbac8316b

# Running

* Run workflow: `dataflows [workflow] [args...]`
* Workflow help: `dataflows [workflow] -h`
* General help: `dataflows -h`
* Show parsed dataflows.yml: `dataflows -c`
* Show version: `dataflows -v`

Examples:

* `dataflows train --model_parameters=1 --data=3 --sessionId=my_session`
* `dataflows predict --pathRData=/code/.RData --pathPredictionData=/code/input/data.csv`
