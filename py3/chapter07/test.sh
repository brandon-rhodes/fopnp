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

runtest srv_simple.py localhost
runtest srv_threaded.py localhost
runtest srv_async.py localhost
runtest srv_legacy1.py localhost
runtest srv_legacy2.py localhost
runtest srv_asyncio1.py localhost
runtest srv_asyncio2.py localhost
