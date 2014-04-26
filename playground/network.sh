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
    image="$1"
    name="$2"
    shift 2
    c=$(docker run --name=$name --hostname=$name --networking=false \
        --dns=10.1.1.1 --dns-search=example.com -d $image)
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
start_bridge playcom

sudo ip link add backbone-isp type veth peer name isp-backbone
sudo ip link add modemA-isp type veth peer name isp-modemA
sudo ip link add modemA-peer type veth peer name modemA-eth1
#sudo ip link add modemB type veth peer name ispB

start_host fopnp/dns backbone backbone-isp
start_host fopnp/base isp isp-backbone isp-modemA
start_host fopnp/base modemA modemA-isp modemA-peer

sudo brctl addif playhome modemA-eth1

sudo ip netns exec $backbone ip addr add 10.1.1.1/32 dev eth0
sudo ip netns exec $backbone ip route add 10.25.1.1/32 dev eth0
sudo ip netns exec $backbone ip route add 10.25.0.0/16 via 10.25.1.1

sudo ip netns exec $isp ip addr add 10.25.1.1/32 dev eth0
sudo ip netns exec $isp ip addr add 10.25.1.1/32 dev eth1
#sudo ip netns exec $isp ip addr add 10.25.1.1/32 dev eth2
sudo ip netns exec $isp ip route add 10.1.1.1/32 dev eth0
sudo ip netns exec $isp ip route add 10.25.1.65/32 dev eth1
#sudo ip netns exec $isp ip route add 10.25.1.66/32 dev eth2
sudo ip netns exec $isp ip route add default via 10.1.1.1

sudo ip netns exec $modemA ip addr add 10.25.1.65/16 dev eth0
sudo ip netns exec $modemA ip addr add 192.168.1.1/24 dev eth1
sudo ip netns exec $modemA ip route add default via 10.25.1.1
sudo ip netns exec $modemA iptables --table nat \
    --append POSTROUTING --out-interface eth0 -j MASQUERADE

echo Ready
read
