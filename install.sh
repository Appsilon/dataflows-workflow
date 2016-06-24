#/bin/bash

if [ -e $DATAFLOWS_DIR ]; then
    cd $DATAFLOWS_DIR
    pip install -r requirements.txt
    ln -s $DATAFLOWS_DIR /usr/bin/dataflows
else 
    echo "Dataflows executable does not exist"
    exit(1)
fi 


