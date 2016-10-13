#!/bin/bash
set -o nounset -o errexit

echo "Installing dataflows from directory: '$DATAFLOWS_DIR'"

if [ -e $DATAFLOWS_DIR ] && [ -e $DATAFLOWS_DIR/dataflows ]; then
    cd $DATAFLOWS_DIR
    pip3.5 install -r requirements.txt
    ln -s $DATAFLOWS_DIR/dataflows /usr/local/bin/dataflows
else 
    echo "Dataflows executable does not exist"
    exit 1
fi 


