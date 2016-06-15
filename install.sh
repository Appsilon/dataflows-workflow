#/bin/bash

DATAFLOWS=`pwd`/dataflows

if [ -e $DATAFLOWS ]; then
    ln -s $DATAFLOWS /usr/bin/dataflows
else 
    echo "Dataflows executable does not exist"
fi 


