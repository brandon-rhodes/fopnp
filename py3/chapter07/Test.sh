#!/bin/bash

function runtest () {
    echo '===========' "$@" '==========='
    python "$@" &
    sleep 1
    python client.py localhost
    kill %1
    wait %1 2>/dev/null || true
    #kill $(lsof | grep 'TCP.*1060' | awk '{print$2}')
}

runtest server_simple.py localhost
