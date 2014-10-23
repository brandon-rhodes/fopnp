#!/bin/sh
#
# Start up the network playground on a boot2docker instance.

sudo mkdir -p /var/run/netns

# Make sure the bridge-control tools are installed.

if [ ! -x /usr/local/sbin/brctl ]
then
    wget ftp://ftp.nl.netbsd.org/vol/2/metalab/distributions/tinycorelinux/4.x/x86/tcz/bridge-utils.tcz
    tce-load -i bridge-utils.tcz
    rm bridge-utils.tcz
fi

# Tool to start a container.

start_container () {
    hostname=$1
    image=$2
    container=${hostname%%.*}

    if docker inspect -f '{{.State.Pid}}' $container &>/dev/null
    then return
    fi

    docker run --name=$container --hostname=$hostname --net=none \
        --dns=10.1.1.1 --dns-search=example.com -d $image

    pid=$(docker inspect -f '{{.State.Pid}}' $container)
    sudo rm -f /var/run/netns/$container
    sudo ln -s /proc/$pid/ns/net /var/run/netns/$container
}

# These commands are each a no-op if the command has already run.

start_bridge () {
    sudo brctl addbr $1 &>/dev/null
}
create_interface () {
    interface=$1
    container=${interface%%-*}
    short_name=${interface##*-}
    sudo ip link add $interface type veth peer name P &>/dev/null || exit
    sudo ip link set P netns $container
    sudo ip netns exec $container ip link set dev P name $short_name
    sudo ip netns exec $container ip link set $short_name up
}
bridge_add_interface () {
    sudo brctl addif $1 $2 &>/dev/null
    sudo ip link set dev $2 up
}

# Build the playground.

start_container h1 fopnp/base
# start h2 fopnp/base
# start h3 fopnp/base
# start h4 fopnp/base
start_container example.com fopnp/base
start_container www.example.com fopnp/www

start_bridge homeA
start_bridge homeB
start_bridge exampleCOM

create_interface example-eth1

#create_interface_pair example-eth1 example-peer
# create_interface_pair www-eth0 www-peer

# bridge_add_interface example-com example-eth1
# bridge_add_interface example-com www-eth0

# give_interface_to_its_container example-eth1
