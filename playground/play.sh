#!/bin/bash

container=h1
ppid=$$

if [ ! -d /proc/sys/net/ipv4/conf/playhome ]
then
    echo "Error: 'network.sh' is not yet up and running"
    exit 1
fi

setup () {

    # At the bottom of this script, our parent process uses "exec" to
    # replace itself with an interactive "docker" whose networking we
    # need to configure.  So, as long as our parent process is still
    # running, we watch for the container to appear.

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

    # The container now exists, so we can configure its networking.

    echo PID is $pid
    sudo ln -s /proc/$pid/ns/net /var/run/netns/$pid
    sudo ip link add $container-eth0 type veth peer name $container-peer
    sudo ip link set $container-peer netns $pid
    sudo ip netns exec $pid ip link set dev $container-peer name eth0
    sudo brctl addif playhome $container-eth0
    sudo rm /var/run/netns/$pid
}

sudo true  # make user type their password before we go into background
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
