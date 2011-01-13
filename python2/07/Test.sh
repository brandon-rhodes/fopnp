#!/bin/bash

for SERVER in server_*.py
do
    echo '===========' $SERVER '==========='
    python $SERVER localhost &
    sleep 1
    python client.py localhost 1060
    kill %1
    wait %1 2>/dev/null || true
    kill $(lsof | grep 'TCP.*1060' | awk '{print$2}')
done
