#!/bin/bash

set -e

if [ $(id -u) != "0" ]
then
    echo 'Error: network.sh must be run as root; try "sudo network.sh"' >&2
    exit 1
fi

stop_everything () {
    for b in $bridges
    do
        ip link set dev $b down
        brctl delbr $b
    done
    for c in $containers
    do
        pid=$(docker inspect -f '{{.State.Pid}}' $c)
        rm -f /var/run/netns/$pid
        echo -n 'Stopping '
        docker stop --time=0 $c
        echo -n 'Removing '
        docker rm $c
    done
}

trap 'exit' SIGINT SIGTERM
trap 'stop_everything' EXIT

start_bridge () {
    brctl addbr $1 || true
    bridges="$bridges $1"
    ip link set dev $1 up
}

start_host () {
    image="$1"
    hostname="$2"
    name=${hostname/.*/}
    shift 2
    c=$(docker run --name=$name --hostname=$hostname --networking=false \
        --dns=10.1.1.1 --dns-search=example.com -d $image)
    containers="$containers $c"
    pid=$(docker inspect -f '{{.State.Pid}}' $c)
    echo $name pid is $pid
    ln -s /proc/$pid/ns/net /var/run/netns/$pid
    for specification in "$@"
    do
        old=${specification/*=/}
        new=${specification/=*/}
        ip link set $old netns $pid
        ip netns exec $pid ip link set dev $old name $new
        ip netns exec $pid ip link set $new up
    done
    eval "$name=$pid"
}

mkdir -p /var/run/netns

# Start up three bridges.  Each bridge serves as a synthetic Ethernet
# network, where students can play with ARP and broadcast and everything
# else that involves hardware addresses and discovery.  Two live over
# beneath the ISP side of the network, while the third serves as the
# internal LAN where the servers of "example.com" live.

start_bridge playhome
start_bridge playhome2
start_bridge playcom

# Build several pairs of linked network interfaces.  When we want to
# construct a simple point-to-point link, we will select two peers and
# throw both of them over the wall into two different containers,
# allowing those two containers to communicate.  When we instead want to
# connect a container to one of our bridges, we will throw only one peer
# over the wall into the container and keep the other peer here in the
# main network namespace where we can add it to the bridge.

ip link add backbone-isp type veth peer name isp-backbone

ip link add modemA-isp type veth peer name isp-modemA
ip link add modemB-isp type veth peer name isp-modemB
ip link add modemA-eth1 type veth peer name modemA-peer
ip link add modemB-eth1 type veth peer name modemB-peer

ip link add backbone-dotcom type veth peer name dotcom-backbone
ip link add dotcom-eth1 type veth peer name dotcom-peer
ip link add ftp-eth0 type veth peer name ftp-peer
ip link add mail-eth0 type veth peer name mail-peer
ip link add www-eth0 type veth peer name www-peer

# Take all of the interfaces that are destined to stay out here, outside
# of any particular container, and connect them to bridges.

brctl addif playhome modemA-eth1
brctl addif playhome2 modemB-eth1
brctl addif playcom dotcom-eth1
brctl addif playcom ftp-eth0
brctl addif playcom mail-eth0
brctl addif playcom www-eth0

# Take all of the other interfaces and throw them over the wall into
# particular containers as we start them running with Docker.

start_host fopnp/dns backbone eth0=backbone-isp eth1=backbone-dotcom
start_host fopnp/base isp eth0=isp-backbone eth1=isp-modemA eth2=isp-modemB
start_host fopnp/base modemA eth0=modemA-isp eth1=modemA-peer
start_host fopnp/base modemB eth0=modemB-isp eth1=modemB-peer
start_host fopnp/base example.com eth0=dotcom-backbone eth1=dotcom-peer
start_host fopnp/ftp ftp.example.com eth0=ftp-peer
start_host fopnp/mail mail.example.com eth0=mail-peer
start_host fopnp/www www.example.com eth0=www-peer

# Okay!  We now have running containers with network interfaces
# successfully installed inside, but none of them know how to talk to
# any of the others.  So we visit each container and set up its IP
# addresses, routes, and (if necessary) IP table rules until everyone
# can talk to everyone else.

ip netns exec $backbone ip addr add 10.1.1.1/32 dev eth0
ip netns exec $backbone ip route add 10.25.1.1/32 dev eth0
ip netns exec $backbone ip route add 10.25.0.0/16 via 10.25.1.1

ip netns exec $isp ip addr add 10.25.1.1/32 dev eth0
ip netns exec $isp ip addr add 10.25.1.1/32 dev eth1
ip netns exec $isp ip addr add 10.25.1.1/32 dev eth2
ip netns exec $isp ip route add 10.1.1.1/32 dev eth0
ip netns exec $isp ip route add 10.25.1.65/32 dev eth1
ip netns exec $isp ip route add 10.25.1.66/32 dev eth2
ip netns exec $isp ip route add default via 10.1.1.1

for modem in $modemA $modemB
do
    ip netns exec $modem ip addr add 10.25.1.65/16 dev eth0
    ip netns exec $modem ip addr add 192.168.1.1/24 dev eth1
    ip netns exec $modem ip route add default via 10.25.1.1
    ip netns exec $modem iptables --table nat \
        --append POSTROUTING --out-interface eth0 -j MASQUERADE
done

ip netns exec $backbone ip addr add 10.1.1.1/32 dev eth1
ip netns exec $backbone ip route add 10.130.1.1/32 dev eth1
ip netns exec $backbone ip route add 10.130.1.0/24 via 10.130.1.1

ip netns exec $example ip addr add 10.130.1.1/32 dev eth0
ip netns exec $example ip route add 10.1.1.1/32 dev eth0
ip netns exec $example ip route add default via 10.1.1.1
ip netns exec $example ip addr add 10.130.1.1/24 dev eth1

ip netns exec $ftp ip addr add 10.130.1.2/24 dev eth0
ip netns exec $ftp ip route add default via 10.130.1.1

ip netns exec $mail ip addr add 10.130.1.3/24 dev eth0
ip netns exec $mail ip route add default via 10.130.1.1

ip netns exec $www ip addr add 10.130.1.4/24 dev eth0
ip netns exec $www ip route add default via 10.130.1.1

echo 'Ready - press Enter or Ctrl-C to shut down the playground network'
read
