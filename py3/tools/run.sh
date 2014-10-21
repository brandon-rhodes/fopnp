#!/bin/bash
#
# Run sample shell code inside a README and rewrite the README with the
# new output.

if [ -z "$1" ]
then
    echo 'usage: run.sh ../chapter01/README.md' >&2
    exit 2
fi

original_directory=$(pwd)

export LANG=C.UTF-8
export PYTHONPATH=$(readlink -f $(dirname $0))/monkeys
export PYTHONDONTWRITEBYTECODE=PLEASE

for readme in "$@"
do
    cd $(dirname $readme)
    while read line
    do
        echo $line
        if [ "$line" = '```' ]
        then
            read command_line
            echo $command_line
            command=${command_line:2}
            eval $command
            read line
            while [ "$line" != '```' ]
            do read line
            done
            echo $line
        fi
    done <$(basename $readme) >$(basename $readme).new 2>&1
    cd $original_directory
    cat $readme.new > $readme
    rm -f $readme.new
done
