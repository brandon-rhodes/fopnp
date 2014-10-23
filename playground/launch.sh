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
start_container h2 fopnp/base
start_container h3 fopnp/base
start_container h4 fopnp/base
start_container modemA fopnp/base
start_container modemB fopnp/base
start_container isp fopnp/base
start_container backbone fopnp/dns
start_container example.com fopnp/base
start_container ftp.example.com fopnp/ftp
start_container mail.example.com fopnp/mail
start_container www.example.com fopnp/www

# For each LAN, create an ethernet bridge and corresponding interfaces.

create_interface h1-eth0
create_interface h2-eth0
create_interface h3-eth0
create_interface h4-eth0
create_interface modemA-eth1
create_interface modemB-eth1

start_bridge homeA

bridge_add_interface homeA modemA-eth1
bridge_add_interface homeA h1-eth0
bridge_add_interface homeA h2-eth0
bridge_add_interface homeA h3-eth0

start_bridge homeB

bridge_add_interface homeB modemB-eth1
bridge_add_interface homeB h1-eth0

create_interface example-eth1
create_interface ftp-eth0
create_interface mail-eth0
create_interface www-eth0

start_bridge exampleCOM

bridge_add_interface exampleCOM example-eth1
bridge_add_interface exampleCOM ftp-eth0
bridge_add_interface exampleCOM mail-eth0
bridge_add_interface exampleCOM www-eth0

# Configure the LAN behind each broadband modem.

for modem in modemA modemB
do
    # sudo ip netns exec $modem ip addr add 10.25.1.65/16 dev eth0
    sudo ip netns exec $modem ip addr add 192.168.1.1/24 dev eth1
    # sudo ip netns exec $modem ip route add default via 10.25.1.1
    # sudo ip netns exec $modem iptables --table nat \
    #     --append POSTROUTING --out-interface eth0 -j MASQUERADE
done

for host in h1 h2 h3 h4
do
    n=${host#?}
    sudo ip netns exec $host ip addr add 192.168.1.1$n/24 dev eth0
    sudo ip netns exec $host ip route add default via 192.168.1.1
done

# Configure the 10.130.1.* network that the example.com machines share.

sudo ip netns exec example ip addr add 10.130.1.1/24 dev eth1
sudo ip netns exec ftp ip addr add 10.130.1.2/24 dev eth0
sudo ip netns exec mail ip addr add 10.130.1.3/24 dev eth0
sudo ip netns exec www ip addr add 10.130.1.4/24 dev eth0
for name in ftp mail www
do sudo ip netns exec $name ip route add default via 10.130.1.1
done
