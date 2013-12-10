#!/bin/bash

for SERVER in server_*.py
do
    echo '===========' $SERVER '==========='
    python $SERVER '' &
    ssh kenaniah <<'EOF'
cd ~/apress
source v/bin/activate
cd fopnp/source/07
LAUNCELOT_SERVER=192.168.5.130 fl-run-bench launcelot_tests.py TestLauncelot.test_dialog > OUT 2>&1
EOF
    kill %1
    wait %1 2>/dev/null
    kill $(lsof | grep 'TCP.*1060' | awk '{print$2}')
    scp kenaniah:apress/fopnp/source/07/bench.xml ~/apress/bench
    (cd ~/apress/bench; fl-build-report --html bench.xml; rm -rf $SERVER; mv test_* $SERVER)
done
