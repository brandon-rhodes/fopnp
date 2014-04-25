#!/bin/bash

set -e

stop_everything () {
    for b in $bridges
    do
        sudo ip link set dev $b down
        sudo brctl delbr $b
    done
    for c in $containers
    do
        pid=$(docker inspect -f '{{.State.Pid}}' $c)
        sudo rm -f /var/run/netns/$pid
        echo -n 'Stopping '
        docker stop --time=0 $c
        echo -n 'Removing '
        docker rm $c
    done
}

trap 'exit' SIGINT SIGTERM
trap 'stop_everything' EXIT

start_bridge () {
    sudo brctl addbr $1 || true
    bridges="$bridges $1"
    sudo ip link set dev $1 up
}

start_host () {
    name="$1"
    shift
    c=$(docker run --name=$name --hostname=$name --networking=false -d \
        fopnp/base /etc/init.d/ssh start -D)
    containers="$containers $c"
    pid=$(docker inspect -f '{{.State.Pid}}' $c)
    echo $name pid is $pid
    sudo ln -s /proc/$pid/ns/net /var/run/netns/$pid
    n=0
    for interface in "$@"
    do
        sudo ip link set $interface netns $pid
        sudo ip netns exec $pid ip link set dev $interface name eth$n
        sudo ip netns exec $pid ip link set eth$n up
        n=$(( $n + 1 ))
    done
    eval "$name=$pid"
}

sudo mkdir -p /var/run/netns

start_bridge playhome
start_bridge playhome2
start_bridge examplecom

sudo ip link add modemA type veth peer name ispA
sudo ip link add modemA-peer type veth peer name modemA-eth1
#sudo ip link add modemB type veth peer name ispB

start_host playmodemA modemA modemA-peer
start_host playisp ispA

sudo brctl addif playhome modemA-eth1

sudo ip netns exec $playmodemA ip addr add 10.25.1.65/32 dev eth0
sudo ip netns exec $playmodemA ip addr add 192.168.1.1/24 dev eth1

read
