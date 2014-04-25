#!/bin/bash

set -e

stop_containers () {
    for c in $containers
    do
        echo -n 'Stopping '
        docker stop --time=0 $c
        echo -n 'Removing '
        docker rm $c
    done
}

trap 'exit' SIGINT SIGTERM
trap 'stop_containers' EXIT

start () {
    name="$1"
    networking=${2:-true}
    c=$(docker run --name=$name --hostname=$name --networking=$networking -d \
        fopnp/base sleep 9999)
    containers="$containers $c"
    eval "$name=$(docker inspect -f '{{.State.Pid}}' $c)"
}

echo hi
sudo brctl addbr playhome
start foo false
start bar
echo foo pid is $foo and bar pid is $bar
read
sudo brctl delbr playhome
echo done

#PID=2343
#ip link set dev eth0 name not_eth0
#docker inspect -f '{{.State.Pid}}' foo
#for bridge in br_home br_home2 br_isp br_backbone
#ln -s /proc/1316/ns/net /var/run/netns/1316
#docker run --networking=false --name=foo --hostname=foo -ti --rm fopnp/base /bin/bash
#docker inspect -f '{{.NetworkSettings.IPAddress}}' foo
