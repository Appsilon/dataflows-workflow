#!/bin/bash

DATAFLOWS=`pwd`/dataflows

pip3.5 install -r requirements.txt

if [ -e $DATAFLOWS ]; then
    sudo ln -s $DATAFLOWS /usr/local/bin/dataflows
else 
    echo "Dataflows executable does not exist"
    exit 1
fi 


