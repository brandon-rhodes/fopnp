#!/bin/bash

container=h1
ppid=$$

if [ ! -d /proc/sys/net/ipv4/conf/playhome ]
then
    echo "Error: 'network.sh' is not yet up and running"
    exit 1
fi

setup () {
    false
    while [ $? = 1 ]
    do
        if ! ps -p $ppid >/dev/null
        then
            echo "play.sh: giving up and exiting, because docker died"
            exit 1
        fi
        sleep .25
        pid=$(docker inspect -f '{{.State.Pid}}' $container 2>/dev/null)
    done
    echo PID is $pid
}

setup &
exec docker run --name=$container --hostname=$container --networking=false \
    --privileged=true --rm -ti fopnp/base /bin/bash

# container=$(docker run --name=h1 --hostname=h1 --networking=true -d \
#     fopnp/base /startup.sh)
# trap 'exit' SIGINT SIGTERM
# trap 'echo && docker stop -t=0 $container && docker rm $container' EXIT
# pid=$(docker inspect -f '{{.State.Pid}}' $container)
# echo $pid ready
# ssh
