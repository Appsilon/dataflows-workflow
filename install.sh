#!/bin/bash

if [ -n "$1" ]; then
  DATAFLOWS_DIR=$1
else
  DATAFLOWS_DIR=`pwd`
fi

echo "Installing dataflows from directory: '$DATAFLOWS_DIR'"

if [ -e $DATAFLOWS_DIR ]; then
  cd $DATAFLOWS_DIR
  pip3.5 install -r requirements.txt
  echo "#!/bin/bash" >> /usr/local/bin/dataflows
  echo "python3.5 $DATAFLOWS_DIR/dataflows.py $@" >> /usr/local/bin/dataflows
  chmod +x /usr/local/bin/dataflows
else 
  echo "Dataflows executable does not exist"
  exit 1
fi 
