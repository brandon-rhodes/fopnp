#!/bin/bash

set -e

container=${1:-h1}
ppid=$$

if [ ! -d /proc/sys/net/ipv4/conf/playhome ]
then
    echo 'Error: 'network.sh' is not yet up and running' >&2
    exit 1
fi

if [ -n "${container/h[1-9]/}" ]
then
    echo 'Error: hostname should be between "h1" and "h9"' >&2
    exit 1
fi

n=${container/h/}

setup () {

    # At the bottom of this script, our parent process uses "exec" to
    # replace itself with an interactive "docker" whose networking we
    # need to configure.  So, as long as our parent process is still
    # running, we watch for the container to appear.

    pid=""
    while [ -z "$pid" ]
    do
        if ! ps -p $ppid >/dev/null
        then
            echo "play.sh: giving up and exiting, because container died"
            exit 1
        fi
        sleep .25
        pid=$(docker inspect -f '{{.State.Pid}}' $container 2>/dev/null ||true)
    done

    # The container now exists, so we can configure its networking.

    sudo ln -s /proc/$pid/ns/net /var/run/netns/$pid
    sudo ip link add $container-eth0 type veth peer name $container-peer
    sudo ip link set $container-peer netns $pid
    sudo ip netns exec $pid ip link set dev $container-peer name eth0
    sudo ip netns exec $pid ip link set dev eth0 up
    sudo ip netns exec $pid ip addr add 192.168.1.1$n/24 dev eth0
    sudo ip netns exec $pid ip route add default via 192.168.1.1
    sudo brctl addif playhome $container-eth0
    sudo rm /var/run/netns/$pid
}

py3=$(readlink -f ../py3)
sudo true  # make user type password before "setup" goes into background
setup &
exec docker run --name=$container --hostname=$container --privileged=true \
     --networking=false --dns=10.1.1.1 --dns-search=example.com \
     --volume=$py3:/py3 --rm -ti fopnp/base /bin/bash
