#!/bin/bash

add-apt-repository ppa:fkrull/deadsnakes
apt-get update
apt-get install python3.5 python3.5-dev libncurses5-dev -y
wget https://bootstrap.pypa.io/get-pip.py
python3.5 get-pip.py
rm get-pip.py
