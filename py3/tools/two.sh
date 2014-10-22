#!/bin/bash
#
# Try running each script through 3to2 to learn which ones can operate
# as network programming examples under Python 2.

set -e

cd $(dirname ${BASH_SOURCE[0]})
cd ..
for chapter in "$@"
do
    two=$(echo $chapter | sed 's/chapter/two/')
    rm -rf $two
    cp -r $chapter $two
    sed 's/\$ python3 /\$ python2 /' $chapter/README.md > $two/README.md
    3to2 -w $two/*.py
    tools/run.sh $two/README.md
    diff -u $chapter/README.md $two/README.md > $two/README.diff
done

# 3to2 -f imports -w two01/*.py
