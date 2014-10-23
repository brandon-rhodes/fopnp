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
        --dns=10.1.1.1 --dns-search=example.com -d $image  >/dev/null

    pid=$(docker inspect -f '{{.State.Pid}}' $container)
    sudo rm -f /var/run/netns/$container
    sudo ln -s /proc/$pid/ns/net /var/run/netns/$container

    echo Container started: $container
}

# These commands are each a no-op if the command has already run.

start_bridge () {
    sudo brctl addbr $1 &>/dev/null || return
    sudo ip link set $1 up
    echo Created bridge: $1
}
create_interface () {
    interface=$1
    container=${interface%%-*}
    short_name=${interface##*-}
    sudo ip link add $interface type veth peer name P &>/dev/null || return
    sudo ip link set P netns $container
    sudo ip netns exec $container ip link set dev P name $short_name
    sudo ip netns exec $container ip link set $short_name up
    echo Created interface: $interface
}
bridge_add_interface () {
    bridge=$1
    interface=$2
    sudo brctl addif $bridge $interface &>/dev/null || return
    sudo ip link set dev $interface up
    echo Bridged interface: $interface
}

# Build the playground.

start_container h1 fopnp/base
# start h2 fopnp/base
# start h3 fopnp/base
# start h4 fopnp/base
start_container example.com fopnp/base
start_container ftp.example.com fopnp/ftp
start_container mail.example.com fopnp/mail
start_container www.example.com fopnp/www

start_bridge homeA
start_bridge homeB
start_bridge exampleCOM

create_interface example-eth1
create_interface ftp-eth0
create_interface mail-eth0
create_interface www-eth0

#create_interface_pair example-eth1 example-peer
# create_interface_pair www-eth0 www-peer

bridge_add_interface exampleCOM example-eth1
bridge_add_interface exampleCOM ftp-eth0
bridge_add_interface exampleCOM mail-eth0
bridge_add_interface exampleCOM www-eth0

# Configure the 10.130.1.* network that the example.com machines share.

sudo ip netns exec example ip addr add 10.130.1.1/24 dev eth1
sudo ip netns exec ftp ip addr add 10.130.1.2/24 dev eth0
sudo ip netns exec mail ip addr add 10.130.1.3/24 dev eth0
sudo ip netns exec www ip addr add 10.130.1.4/24 dev eth0
for name in ftp mail www
do sudo ip netns exec $name ip route add default via 10.130.1.1
done
